INSTALLED_APPS = (
    "django.contrib.auth",
    # "django.contrib.admin",
    "django.contrib.admin.apps.SimpleAdminConfig",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "apps.books",

)

DRF_PACKAGES = (
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "knox",
    "drf_spectacular",
    "dj_rest_auth.registration",
)

LOCAL_APPS = (
)

THIRD_PARTY = (
    "django_extensions",
    "django_probes",  # wait for DB to be ready to accept connections
)

INSTALLED_APPS += LOCAL_APPS + DRF_PACKAGES + THIRD_PARTY
