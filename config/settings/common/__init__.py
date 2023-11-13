from .cors import *
from .databases import *
from .drf import *
from .installed_apps import *
from .middleware import *
from .paths import *
from .security import *
from .static import *
from .templates import *

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

APP_LABEL = "ocelot"
