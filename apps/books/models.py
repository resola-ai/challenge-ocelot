# models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(DjangoUserManager):
    """Adjusted user manager that works w/o `username` field."""

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create superuser instance (used by `createsuperuser` cmd)."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):

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
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
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
