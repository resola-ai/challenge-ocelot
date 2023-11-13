from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """Default configuration for Users app."""
    name = "apps.books"

    def ready(self):
        # pylint: disable=unused-import
        from .api import scheme  # noqa
