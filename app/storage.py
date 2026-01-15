import os
import uuid
from azure.storage.blob import BlobServiceClient, ContentSettings

BLOB_CONNECTION_STRING = os.environ.get("BLOB_CONNECTION_STRING")
BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER")

blob_service_client = BlobServiceClient.from_connection_string(
    BLOB_CONNECTION_STRING
)

def upload_image(image):
    # Safety checks
    if not image or image.filename == "":
        raise ValueError("Invalid image")

    # Reset stream pointer (CRITICAL)
    image.stream.seek(0)

    # Generate safe unique blob name
    extension = os.path.splitext(image.filename)[1]
    blob_name = f"{uuid.uuid4()}{extension}"

    blob_client = blob_service_client.get_blob_client(
        container=BLOB_CONTAINER,
        blob=blob_name
    )

    blob_client.upload_blob(
        image.stream,
        overwrite=True,
        content_settings=ContentSettings(
            content_type=image.content_type
        )
    )

    return blob_client.url

