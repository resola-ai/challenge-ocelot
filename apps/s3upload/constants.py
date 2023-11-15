from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class FileContentType(TextChoices):
    """Available content types for files."""
    IMAGE = "image", _("image")
    VIDEO = "video", _("video")
