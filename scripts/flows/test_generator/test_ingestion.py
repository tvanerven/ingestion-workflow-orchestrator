import logging
import os
from random import randint

import requests
from prefect import flow, task, get_run_logger
from flows.test_generator.factories import AssetFactory, AuthorFactory, ContactFactory
from flows.test_generator.mapping import STANDART_MAPPING
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
def map_asset_metadata(asset):
    """
    Task to map the generated asset metadata using a predefined mapping.
    """
    logger = get_run_logger()

    response = requests.post(
        url='http://dataversemapper:8082/mapper',
        json={
            'metadata': asset, 
            'template': STANDARD_TEMPLATE,
            'mapping': STANDART_MAPPING,
        }
    )
    mapped_metadata = response.json()
    logger.info("Mapped data: %s", mapped_metadata)
    return mapped_metadata

@task
def import_asset_to_dataverse(mapped_metadata, doi):
    """
    Task to import the mapped metadata into Dataverse.
    """
    logger = get_run_logger()

    response = requests.post(
        url='http://dataverseimporter:8989/importer',
        json={
            # 'doi': f'doi:{doi}', 
            'metadata': mapped_metadata,
            'dataverse_information': {
                'base_url': os.environ.get('DATAVERSE_URL'),
                'dt_alias': 'test',
                'api_token': os.environ.get('DATAVERSE_API_TOKEN'),
            },
        }
    )
    logger.info("Import response: %s", response.json())
    return response.json()

@flow
def main():
    asset = generate_test_asset()
    mapped_metadata = map_asset_metadata(asset)
    doi = asset['doi'].split('https://doi.org/')[-1]  # Extract DOI from URL

    response = import_asset_to_dataverse(
        mapped_metadata=mapped_metadata, 
        doi=doi
    )
    return response


if __name__ == "__main__":
    main()