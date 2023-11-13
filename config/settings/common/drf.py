from datetime import timedelta

# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = dict(
    DEFAULT_AUTHENTICATION_CLASSES=("knox.auth.TokenAuthentication",),
    DEFAULT_PERMISSION_CLASSES=("rest_framework.permissions.AllowAny",),
    DEFAULT_RENDERER_CLASSES=(
        "rest_framework.renderers.JSONRenderer",
        # "libs.api.renderers.CustomBrowsableAPIRenderer",
    ),
    DEFAULT_SCHEMA_CLASS="drf_spectacular.openapi.AutoSchema",
    DEFAULT_FILTER_BACKENDS=(
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
    DEFAULT_PAGINATION_CLASS="rest_framework.pagination.LimitOffsetPagination",
    PAGE_SIZE=25,
    TEST_REQUEST_DEFAULT_FORMAT="json",
)

# https://james1345.github.io/django-rest-knox/settings/
REST_KNOX = dict(
    SECURE_HASH_ALGORITHM="cryptography.hazmat.primitives.hashes.SHA512",
    AUTH_TOKEN_CHARACTER_LENGTH=64,
    TOKEN_TTL=timedelta(weeks=2),
    TOKEN_LIMIT_PER_USER=None,
    AUTO_REFRESH=False,
    USER_SERIALIZER="apps.books.api.serializers.UserSerializer",
)

# https://drf-spectacular.readthedocs.io/en/latest/settings.html
SPECTACULAR_SETTINGS = dict(
    TITLE="ocelot Api",
    DESCRIPTION="",

)
# from knox.auth import TokenAuthentication
