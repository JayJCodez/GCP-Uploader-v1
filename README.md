# 🌐 GCP Storage Manager

This project provides a command-line interface (CLI) for managing files in Google Cloud Storage (GCS). 🚀 You can upload files, view blobs in a bucket, and delete specific blobs using this tool.

## 📑 Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Contributing](#contributing)
6. [License](#license)

## ✨ Features

- **📤 Upload Files**: Upload files to a specified GCS bucket and make them publicly accessible.
- **👁️ View Blobs**: List all blobs in a specified GCS bucket with details such as size, content type, and public URL.
- **🗑️ Delete Blobs**: Delete specific blobs from a GCS bucket by selecting them from a list.

## 🚀 Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/JayJCodez/GCP-Uploader-v1.git
    cd gcp-storage-manager
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` File**:
    Create a `.env` file in the root of your project directory with the following content:
    ```env
    SERVICE_ACCOUNT_KEY_PATH=path/to/your/service_account_key.json
    BUCKET_NAME=your-bucket-name
    ```

## 🛠️ Usage

1. **📤 Upload a File**:
    ```bash
    python main.py
    ```
    Follow the prompts to specify the file path and destination blob name.

2. **👁️ View Blobs**:
    ```bash
    python main.py
    ```
    Choose the option to view blobs to list all blobs in the bucket.

3. **🗑️ Delete Blobs**:
    ```bash
    python main.py
    ```
    Choose the option to delete files, then select the blobs to delete by entering their numbers.

## 🔧 Configuration

Ensure that your `.env` file contains the correct paths and bucket name:

- `SERVICE_ACCOUNT_KEY_PATH`: The path to your GCP service account key file.
- `BUCKET_NAME`: The name of your GCS bucket.

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to replace placeholders like `https://github.com/yourusername/gcp-storage-manager.git` with your actual repository URL, and adjust instructions as needed for your specific project setup. 🎉