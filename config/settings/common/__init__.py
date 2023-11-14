from .cors import *
from .databases import *
from .drf import *
from .installed_apps import *
from .middleware import *
from .paths import *
from .security import *
from .static import *
from .templates import *
from .storage import *

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

APP_LABEL = "ocelot"

# Limit for allowed file size in bytes
ATTACHMENTS_SIZE_LIMIT = 5 * 1024 * 1024  # 5 megabytes

FILE_PATH_TEMPLATE = "{destination}{name}.{extension}"
