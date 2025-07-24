from prefect import flow, task, get_run_logger
import requests

@flow(name="Submit dataset for review")
def main(doi: str = "dataset_doi", dataverse_api_token: str = "yourtoken"):
    logger = get_run_logger()
    response = requests.post(
        url=f"https://fairvault.dev.ugent.be/api/datasets/:persistentId/submitForReview?persistentId={doi}",
        headers={
            "X-Dataverse-key": dataverse_api_token,
            "Content-Type": "application/json"
        },
    )
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response body: {response.json()}")

if __name__ == "__main__":
    main.from_source(
        source="/app/scripts/flows/test_generator",
        entrypoint="submit_for_review.py:main"
    ).deploy(
        name="Submit dataset for review",
        work_pool_name='default',
        tags=["test", "ingestion", "dataset"],
        parameters={
            'doi': 'dataset_doi',
            'dataverse_api_token': 'yourtoken'
        },
    )