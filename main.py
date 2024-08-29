from gcp_manager import upload_to_gcp, view_gcp_bucket, delete_blobs


def main():
    """Main function to handle user input and actions."""
    option = input(
        "What would you like to do? \n1. View Blobs\n2. Upload new blob\n3. Delete files from GCP\n"
    )

    try:
        option = int(option)
        if option == 1:
            view_gcp_bucket()
        elif option == 2:
            source_file_name = input("Please enter the path of your file: \n")
            destination_blob_name = input(
                "Enter the preferred path of this object specifying new directories with a slash ('/')\n"
            )
            upload_to_gcp(source_file_name, destination_blob_name)
        elif option == 3:
            delete_blobs()
        else:
            print("Invalid selection. Please choose either 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
