INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
)

DRF_PACKAGES = (
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "knox",
    "drf_spectacular",
)

LOCAL_APPS = (
    "apps.books",
)

THIRD_PARTY = (
    "django_extensions",
)

INSTALLED_APPS += LOCAL_APPS + DRF_PACKAGES + THIRD_PARTY
