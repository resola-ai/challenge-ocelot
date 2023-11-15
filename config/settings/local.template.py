from .common import *

FRONTEND_URL = ""
ENVIRONMENT = "local"
DEBUG = True


INTERNAL_IPS = (
    "0.0.0.0",
    "127.0.0.1",
)

DATABASES["default"].update(
    NAME="challenge-ocelet-dev",
    USER="challenge-ocelet-user",
    PASSWORD="manager",
    HOST="postgres",
    PORT="5432",
    CONN_MAX_AGE=0,
)


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = ""
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# disable any password restrictions
AUTH_PASSWORD_VALIDATORS = []

MIDDLEWARE += (
    "corsheaders.middleware.CorsMiddleware",
)

INSTALLED_APPS += (
    'django_probes',  # wait for DB to be ready to accept connections
    "corsheaders",    # provide CORS for local development
)

AUTH_USER_MODEL = "books.User"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
