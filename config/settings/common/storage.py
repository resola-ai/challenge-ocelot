from apps.s3upload.constants import FileContentType


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
}

# Limit for allowed file size in bytes
ATTACHMENTS_SIZE_LIMIT = 5 * 1024 * 1024  # 5 megabytes

FILE_PATH_TEMPLATE = "{type_folder}/{destination}/{name}.{extension}"

# Map for folders for each content type
CONTENT_TYPE_FOLDERS = {
    FileContentType.IMAGE: "images",
    FileContentType.VIDEO: "videos",
}

BUCKET_FOLDERS = (
    r"books",
)
