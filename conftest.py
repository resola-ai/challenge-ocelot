"""Configuration file for pytest
"""
import pytest
from django.conf import settings
from rest_framework.test import APIClient

from apps.books.factories import BookFactory, StaffFactory


def pytest_configure():
    """Set up Django settings for tests.

    `pytest` automatically calls this function once when tests are run.
    """
    settings.DEBUG = False
    settings.TESTING = True

    # The default password hasher is rather slow by design.
    # https://docs.djangoproject.com/en/dev/topics/testing/overview/
    settings.PASSWORD_HASHERS = (
        "django.contrib.auth.hashers.MD5PasswordHasher",
    )
    settings.EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    # To disable celery in tests
    settings.CELERY_TASK_ALWAYS_EAGER = True

    # Set server name so that we can set correct file path for uploaded files
    settings.SERVER_NAME = "testserver.local"
    settings.DEFAULT_FILE_STORAGE = (
        "django.core.files.storage.FileSystemStorage"
    )

    # Use a test prefix so that unittest does not affect main redis app
    settings.CACHES["default"]["KEY_PREFIX"] = "test"


@pytest.fixture(scope="session", autouse=True)
def django_db_setup(django_db_setup):
    """Set up test db for testing."""


@pytest.fixture(autouse=True)
# pylint: disable=invalid-name
def enable_db_access_for_all_tests(django_db_setup, db):
    """This hook allows all tests to access DB."""


@pytest.fixture(scope="session", autouse=True)
def temp_directory_for_media(tmpdir_factory):
    """Fixture that set temp directory for all media files.

    This fixture changes FILE_STORAGE to filesystem and provides temp dir for
    media. PyTest cleans up this temp dir by itself after few test runs
    """

    media = tmpdir_factory.mktemp("tmp_media")
    settings.MEDIA_ROOT = media


@pytest.fixture(scope="session")
def authenticated_api_client(django_db_blocker):
    """Return API Client for authenticated user."""
    with django_db_blocker.unblock():
        user = StaffFactory()
    client = APIClient()
    client.force_authenticate(user)
    return client


@pytest.fixture
def unauthenticated_api_client():
    """Return an unauthenticated API Client."""
    return APIClient()


@pytest.fixture(scope="session")
def book(django_db_blocker):
    with django_db_blocker.unblock():
        return BookFactory()
