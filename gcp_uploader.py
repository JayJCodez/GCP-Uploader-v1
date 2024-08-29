from google.cloud import storage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use the actual path to your service account JSON key file
SERVICE_ACCOUNT_KEY_PATH = os.getenv("SERVICE_ACCOUNT_KEY_PATH")
bucket_name = os.getenv("BUCKET_NAME")


def upload_to_gcp(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket and makes it public."""
    # Initialize a GCP Storage client with the service account key file
    storage_client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_KEY_PATH)

    # Get the bucket object
    bucket = storage_client.bucket(bucket_name)

    # Create a blob (file) object in the bucket
    blob = bucket.blob(destination_blob_name)

    # Upload the file to GCP
    blob.upload_from_filename(source_file_name)

    # Make the file publicly accessible
    blob.make_public()

    print(
        f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}."
    )
    print(f"The file is publicly accessible at {blob.public_url}")


def optionHandler(prompt: str):
    return input(prompt)


def view_gcp_bucket():
    client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_KEY_PATH)

    client._delete_resource()

    try:
        bucket = client.bucket(bucket_name)
        blobs = bucket.list_blobs()

        print("Blobs in bucket:")
        for blob in blobs:
            print(f"Name: {blob.name}")
            print(f"Size: {blob.size / 1048576 } MB")
            print(f"Content Type: {blob.content_type}")
            print(f"Updated: {blob.updated}")
            print(f"Created: {blob.time_created}")
            print(f"CRC32C: {blob.crc32c}")
            print(f"MD5 Hash: {blob.md5_hash}")
            print(f"Public URL: {blob.public_url}")
            print("Custom Metadata:")
            if blob.metadata:
                for key, value in blob.metadata.items():
                    print(f"  {key}: {value}")
            else:
                print("  No custom metadata.")
            print("-" * 40)
    except Exception as e:
        print(f"An error occurred: {e}")


def deleteBlob():
    client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_KEY_PATH)

    bucket = client.bucket(bucket_name)

    # List all blobs in the bucket and display them (for user reference)
    blobs = bucket.list_blobs()
    for blob in blobs:
        print(f"Blob Name: {blob.name}")
        print(f"Size: {blob.size / 1048576} MB")
        print(f"Content Type: {blob.content_type}")
        print(f"Updated: {blob.updated}")
        print(f"Created: {blob.time_created}")
        print(f"CRC32C: {blob.crc32c}")
        print(f"MD5 Hash: {blob.md5_hash}")
        print(f"Public URL: {blob.public_url}")
        print("-" * 40)

    # Prompt user for file paths
    file_paths = optionHandler(
        "Enter the path of the files with a comma (',') in-between for multiple file deletion\n"
    )

    # Split the file paths into a list and strip any extra spaces
    formatted_paths = [path.strip() for path in file_paths.split(",")]

    try:
        # Delete the blobs listed in formatted_paths
        bucket.delete_blobs(formatted_paths)
        print(f"Successfully deleted files: {formatted_paths}")
    except Exception as e:
        print(f"An error occurred while deleting files: {e}")


if __name__ == "__main__":
    option = optionHandler(
        "What would you like to do? \n1. View Blobs\n2. Upload new blob\nUse the numbers as a selection\n3. Delete files from GCP\n"
    )

    try:
        if int(option) == 1:
            view_gcp_bucket()
        elif int(option) == 2:
            bucket_name = optionHandler("Please enter your bucket name: \n")
            source_file_name = optionHandler("Please enter the path of your file: \n")
            destination_blob_name = optionHandler(
                "Enter the preferred path of this object specifiying new directories with a slash ('/')\n"
            )
        elif int(option) == 3:
            deleteBlob()
        else:
            print("Invalid selection. Please choose either 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")
