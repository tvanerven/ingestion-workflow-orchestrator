import json
import os
from random import choice, randint

import requests
import utils

from prefect import flow, task, get_run_logger
from configuration.config import settings
from flows.test_generator.factories import AssetFactory, AuthorFactory, ContactFactory
from flows.test_generator.mapping import STANDARD_MAPPING
from flows.test_generator.template import STANDARD_TEMPLATE

@task
def generate_test_asset():
    """
    Task to generate a test asset with random authors and contacts.
    """
    logger = get_run_logger()

    asset = AssetFactory(
        dataset_contacts=[
            ContactFactory() for _ in range(randint(1, 3))
        ],
        authors=[
            AuthorFactory() for _ in range(randint(1, 3))
        ]
    )
    logger.info("Generated asset: %s", asset)
    return asset

@task
def map_asset_metadata(asset: dict):
    """
    Task to map the generated asset metadata using a predefined mapping.
    """
    logger = get_run_logger()

    response = requests.post(
        url='https://dataversemapper.wizardtower.dev/mapper',
        json={
            'metadata': asset, 
            'template': STANDARD_TEMPLATE,
            'mapping': STANDARD_MAPPING,
        }
    )
    mapped_metadata = response.json()
    logger.info("Mapped data: %s", mapped_metadata)
    return mapped_metadata

@task
def import_asset_to_dataverse(mapped_metadata: dict, dt_alias: str = 'test', dataverse_api_token: str = 'yourtoken'):
    """
    Task to import the mapped metadata into Dataverse.
    """
    logger = get_run_logger()

    response = requests.post(
        url='https://dataverse-importer.wizardtower.dev/importer',
        json={
            'metadata': mapped_metadata,
            'dataverse_information': {
                'base_url': "https://fairvault.dev.ugent.be",
                'dt_alias': dt_alias,
                'api_token': dataverse_api_token,
            },
        }
    )
    logger.info("Import response: %s", response.json())
    return response.json()

@task
def upload_file(persistent_id: str, dt_alias: str = 'test', dataverse_api_token: str = 'yourtoken'):
    logger = get_run_logger()
    minio_client = utils.create_s3_client()
    settings_dict = settings.TEST

    # Define the file path and bucket name
    paginator = minio_client.get_paginator("list_objects_v2")
    bucket = settings_dict.BUCKET_NAME
    pages = paginator.paginate(
        Bucket=bucket,
    )
    all_files = [obj for page in pages for obj in page.get("Contents", [])]
    if not all_files:
        logger.error("No files found in the bucket.")
        return
    
    file_ = choice(all_files)
    file_name = file_["Key"]
    object_data = minio_client.get_object(
        Bucket=bucket,
        Key=file_name
    )
    metadata = object_data['Body'].read()
    logger.info(
        f"Retrieved file: {file_name}, Size: {len(metadata)}"
    )

    response = requests.post(
        url='https://dataverse-importer.wizardtower.dev/file-upload',
        data={
            'json_data': json.dumps({
                'doi': persistent_id, 
                'dataverse_information': {
                    'base_url': "https://fairvault.dev.ugent.be",
                    'dt_alias': dt_alias,
                    'api_token': dataverse_api_token,
                },
            })
        },
        files={'file': (file_name, metadata)}
    )
    logger.info("File upload response: %s", response.json())
    return response.json()


@flow(name="Test Ingestion Pipeline")
def main(dt_alias: str = 'test', dataverse_api_token: str = 'yourtoken'):
    asset = generate_test_asset()
    mapped_metadata = map_asset_metadata(asset)

    import_response = import_asset_to_dataverse(
        mapped_metadata=mapped_metadata,
        dt_alias=dt_alias,
        dataverse_api_token=dataverse_api_token
    )
    
    dataset_persistent_id = import_response.get('data', {}).get('persistentId')
    response = upload_file(dataset_persistent_id, dt_alias=dt_alias, dataverse_api_token=dataverse_api_token)

    return response

if __name__ == "__main__":
    main.from_source(
        source="/app/scripts/flows/test_generator",
        entrypoint="test_ingestion.py:main"
    ).deploy(
        name="Test Ingestion Pipeline",
        work_pool_name='default',
        tags=["test", "ingestion"],
        parameters={
            'dt_alias': 'test',
            'dataverse_api_token': 'yourtoken'
        },
    )