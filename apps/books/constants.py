from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class BookGenre(TextChoices):
    UNCLASSIFIED =  "Unclassified", _("Unclassified")
    SCIENTIFIC = "Scientific", _("Scientific")
    NOVEL = "Novel", _("Novel")
