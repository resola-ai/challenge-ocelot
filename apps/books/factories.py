import uuid

import factory
from django.conf import settings

from . import models

DEFAULT_PASSWORD = "Test111!"


class StaffFactory(factory.django.DjangoModelFactory):
    """Factory to generate test staff instance."""

    first_name = factory.Faker("first_name")
    password = factory.PostGenerationMethodCall(
        "set_password",
        DEFAULT_PASSWORD,
    )

    class Meta:
        model = models.User

    @factory.lazy_attribute
    def email(self):
        """Return formatted email."""
        return (
            f"{uuid.uuid4()}@"
            f"{settings.APP_LABEL.lower().replace(' ', '-')}.com"
        )


class AuthorFactory(factory.django.DjangoModelFactory):
    """Factory to generate test author instance."""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    class Meta:
        model = models.User


class BookFactory(factory.django.DjangoModelFactory):
    """Factory to generate test book instance."""

    title = factory.Faker('sentence', nb_words=4)
    publish_date = factory.Faker('date_object')
    isbn = factory.Faker('isbn10')

    class Meta:
        model = models.Book
