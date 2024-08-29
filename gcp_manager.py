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
        logging.error(f"Failed to initialize storage client: {e} 🚫")
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
            f"File {source_file_name} uploaded to {destination_blob_name} in bucket {BUCKET_NAME} 📤."
        )
        logging.info(f"The file is publicly accessible at {blob.public_url} 🌐")
    except Exception as e:
        logging.error(f"Failed to upload file {source_file_name}: {e} 🚫")
        raise


def view_gcp_bucket():
    """Displays all blobs in the GCP bucket."""
    client = initialize_storage_client()

    try:
        bucket = client.bucket(BUCKET_NAME)
        blobs = list(bucket.list_blobs())

        if not blobs:
            logging.info("No blobs found in the bucket. 🗂️")
            return

        logging.info("Blobs in bucket:")
        for idx, blob in enumerate(blobs, start=1):
            logging.info(
                f"{idx}. Name: {blob.name}, Size: {blob.size / 1048576:.2f} MB, Updated: {blob.updated}, Public URL: {blob.public_url} 📋"
            )

    except Exception as e:
        logging.error(f"An error occurred while listing blobs: {e} 🚫")
        raise


def delete_blobs():
    """Deletes specified blobs from the GCP bucket."""
    client = initialize_storage_client()
    bucket = client.bucket(BUCKET_NAME)

    try:
        blobs = list(bucket.list_blobs())

        if not blobs:
            logging.info("No blobs found to delete. 🗑️")
            return

        logging.info("Blobs available for deletion:")
        blob_dict = {}
        for idx, blob in enumerate(blobs, start=1):
            logging.info(f"{idx}. Name: {blob.name}")
            blob_dict[idx] = blob

        file_numbers = input(
            "Enter the numbers of the files you want to delete, separated by commas (e.g., 1,3,5):\n"
        )

        # Parse and strip numbers
        selected_indices = [
            int(num.strip()) for num in file_numbers.split(",") if num.strip().isdigit()
        ]
        selected_blobs = [
            blob_dict[idx] for idx in selected_indices if idx in blob_dict
        ]

        if not selected_blobs:
            logging.info("No valid blobs selected for deletion. 🚫")
            return

        # Delete selected blobs
        bucket.delete_blobs(selected_blobs)
        logging.info(
            f"Successfully deleted blobs: {[blob.name for blob in selected_blobs]} ✅"
        )

    except Exception as e:
        logging.error(f"An error occurred while deleting files: {e} 🚫")
        raise
