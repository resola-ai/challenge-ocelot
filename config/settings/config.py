import environ

from .common import *  # noqa

env = environ.Env()

env.read_env()

# when variable is not present in secret manager, it's filled with this
# constant in .env file
ENV_NOTSET = "<no value>"

DEBUG = env.bool("DEBUG", default=False)

ENVIRONMENT = env.str("ENVIRONMENT", default="")

FRONTEND_URL = env.str("FRONTEND_URL", default="")

BACKEND_URL = env.str("BACKEND_URL", default="localhost:8000")

# ------------------------------------------------------------------------------
# DATABASES - PostgreSQL
# ------------------------------------------------------------------------------
DATABASES["default"].update(  # noqa
    ENGINE=env.str("DB_ENGINE"),
    NAME=env.str("RDS_DB_NAME"),
    USER=env.str("RDS_DB_USER"),
    PASSWORD=env.str("RDS_DB_PASSWORD"),
    HOST=env.str("RDS_DB_HOST"),
    PORT=env.str("RDS_DB_PORT"),
)

# ------------------------------------------------------------------------------
# AWS S3 - Django Storages S3
# ------------------------------------------------------------------------------
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env.str("AWS_S3_DIRECT_REGION")
AWS_S3_ENDPOINT_URL = f"https://s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_DEFAULT_ACL = "public-read"
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
AWS_ROLE_ARN = env.str("AWS_ROLE_ARN")
AWS_SESSION_NAME = 'AssumeRoleSession'

# ------------------------------------------------------------------------------
# DJANGO SECURITY
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# ------------------------------------------------------------------------------
SECRET_KEY = env.str("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += (
    'django_probes',  # wait for DB to be ready to accept connections
)

AUTH_USER_MODEL = "books.User"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
