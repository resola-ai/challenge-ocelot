from django.apps import AppConfig


class CoreAppConfig(AppConfig):
    """Default configuration for Core app."""

    name = "apps.s3upload"

    def ready(self):
        # pylint: disable=unused-import
        from .api import scheme  # noqa
