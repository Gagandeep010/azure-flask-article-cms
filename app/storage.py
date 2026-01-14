from azure.storage.blob import BlobServiceClient
import uuid
import os

def upload_image(file, connection_string, container_name):
    blob_service = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service.get_container_client(container_name)

    # Ensure temp folder exists
    os.makedirs("temp", exist_ok=True)

    filename = f"{uuid.uuid4()}-{file.filename}"
    temp_path = os.path.join("temp", filename)

    # 1️⃣ Save locally
    file.save(temp_path)

    # 2️⃣ Upload using file handle (THIS IS THE KEY)
    with open(temp_path, "rb") as data:
        container_client.upload_blob(
            name=filename,
            data=data,
            overwrite=True
        )

    # 3️⃣ Cleanup
    os.remove(temp_path)

    return f"{container_client.url}/{filename}"
