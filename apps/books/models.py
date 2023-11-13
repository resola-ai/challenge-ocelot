# models.py
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    email = models.CharField(
        verbose_name=_("Email address"),
        max_length=254,  # to be compliant with RFCs 3696 and 5321
        blank=True,
        null=True,
        unique=True,
        validators=[validators.validate_email],
    )
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=80,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=80,
        blank=True,
    )

    objects = UserManager()


class Author(User):

    class Meta:
        proxy = True


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        related_name='own_books',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    publish_date = models.DateField()
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
