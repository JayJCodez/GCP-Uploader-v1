import os
import logging
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants for environment variables
SERVICE_ACCOUNT_KEY_PATH = os.getenv("SERVICE_ACCOUNT_KEY_PATH")
BUCKET_NAME = os.getenv("BUCKET_NAME")


def initialize_storage_client():
    """Initializes and returns a GCP storage client."""
    try:
        return storage.Client.from_service_account_json(SERVICE_ACCOUNT_KEY_PATH)
    except Exception as e:
        logging.error(f"Failed to initialize storage client: {e}")
        raise


def upload_to_gcp(source_file_name, destination_blob_name):
    """Uploads a file to the GCP bucket and makes it public."""
    client = initialize_storage_client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)

    try:
        blob.upload_from_filename(source_file_name)
        blob.make_public()
        logging.info(
            f"File {source_file_name} uploaded to {destination_blob_name} in bucket {BUCKET_NAME}."
        )
        logging.info(f"The file is publicly accessible at {blob.public_url}")
    except Exception as e:
        logging.error(f"Failed to upload file {source_file_name}: {e}")
        raise


def view_gcp_bucket():
    """Displays all blobs in the GCP bucket."""
    client = initialize_storage_client()

    try:
        bucket = client.bucket(BUCKET_NAME)
        blobs = bucket.list_blobs()

        logging.info("Blobs in bucket:")
        for blob in blobs:
            logging.info(
                f"Name: {blob.name}, Size: {blob.size / 1048576} MB, Updated: {blob.updated}, Public URL: {blob.public_url}"
            )
            logging.info("-" * 40)
    except Exception as e:
        logging.error(f"An error occurred while listing blobs: {e}")
        raise


def delete_blobs():
    """Deletes specified blobs from the GCP bucket."""
    client = initialize_storage_client()
    bucket = client.bucket(BUCKET_NAME)

    try:
        blobs = bucket.list_blobs()
        logging.info("Blobs in bucket:")
        for blob in blobs:
            logging.info(
                f"Name: {blob.name}, Size: {blob.size / 1048576} MB, Updated: {blob.updated}, Public URL: {blob.public_url}"
            )
            logging.info("-" * 40)

        file_paths = input(
            "Enter the path of the files with a comma (',') in-between for multiple file deletion\n"
        )
        formatted_paths = [path.strip() for path in file_paths.split(",")]

        bucket.delete_blobs(formatted_paths)
        logging.info(f"Successfully deleted files: {formatted_paths}")
    except Exception as e:
        logging.error(f"An error occurred while deleting files: {e}")
        raise
