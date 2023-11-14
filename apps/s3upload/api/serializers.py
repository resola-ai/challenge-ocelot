from urllib.parse import urlparse

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers


class S3SignedUrlRequestSerializer(serializers.Serializer):
    """Serializer to form file path."""

    destination = serializers.CharField(
        max_length=250,
        required=True,
    )
    extension = serializers.CharField(
        max_length=5,
        required=True,
    )


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Example 1",
            summary="S3 Presigned URL Response",
            description="""The response include url and
            list of credential to upload file""",
            value={
                "url": "https://hlogs-bucket.s3.amazonaws.com/",
                "fields": {
                    "success_action_status": 201,
                    "acl": "public-read",
                    "key": "images/user/1/example.strin",
                    "AWSAccessKeyId": "EXAMPLEKEY",
                    "x-amz-security-token": "exampletoken",
                    "signature": "examplesignature",
                },
            },
            response_only=True,
        ),
    ],
)
class S3SignedUrlResponseSerializer(serializers.Serializer):
    """Serializer for S3 Signed URL response.

    Attributes:
        url (str): url for uploading file.
        field (JSON): Set of credentials to upload file
    """
    url = serializers.CharField()
    field = serializers.JSONField()


class S3DirectUploadURLField(serializers.URLField):
    """URL serializer field for S3 object."""
    def __init__(self, **kwargs):
        """Custom initialization.

        Add URLValidator to self, but don't add it to self.validators, because
        now validation is called after `to_internal_value`. So it provides
        validation before `to_internal_value`.
        """
        # pylint: disable=E1003
        super(serializers.URLField, self).__init__(**kwargs)
        self.validator = URLValidator(message=self.error_messages["invalid"])

    def to_internal_value(self, data):
        """Validate `data` and convert it to internal value.

        Cut domain from url to save it in file field.

        """
        if not isinstance(data, str):
            self.fail("invalid")
        self.validator(data)

        # Crop server domain and port and get relative path to avatar
        file_url = urlparse(data).path
        if file_url.startswith(settings.MEDIA_URL):
            # In case of local storing crop the media prefix
            file_url = file_url[len(settings.MEDIA_URL):]
        elif (
            settings.AWS_STORAGE_BUCKET_NAME and
            settings.AWS_STORAGE_BUCKET_NAME in file_url
        ):
            # In case of S3 upload crop S3 bucket name
            file_url = file_url.split(
                f"{settings.AWS_STORAGE_BUCKET_NAME}/",
            )[-1]
        if not default_storage.exists(file_url):
            raise serializers.ValidationError(
                _("File does not exist."),
            )
        return file_url

    def to_representation(self, value):
        """Return full file url."""
        if not getattr(value, "url", None):
            # If the file has not been saved it may not have a URL.
            return None
        url = value.url
        request = self.context.get("request", None)
        if request is not None:
            return request.build_absolute_uri(url)
        return value.name
