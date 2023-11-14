from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.s3upload.api.serializers import S3SignedUrlResponseSerializer
from apps.s3upload.api.views import S3PresignedUrlView

extend_schema_view(
    post=extend_schema(
        responses=S3SignedUrlResponseSerializer,
    ),
)(S3PresignedUrlView)
