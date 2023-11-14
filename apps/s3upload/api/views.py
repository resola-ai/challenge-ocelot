import uuid

from botocore.exceptions import ClientError
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.s3upload.utils import create_presigned_url

from . import serializers


class S3PresignedUrlView(APIView):
    """Endpoint to generate links for direct uploading files to S3."""

    serializer_class = serializers.S3SignedUrlRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        params = {"name": uuid.uuid4()}
        params.update(serializer.data)

        object_path = settings.FILE_PATH_TEMPLATE.format(**params)

        try:
            presigned_url = create_presigned_url(
                bucket_name=settings.AWS_STORAGE_BUCKET_NAME,
                object_name=object_path,
                expiration=3600,
            )
            return Response(data=presigned_url)
        except ClientError:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"detail": "Something wrong, try later"},
            )
