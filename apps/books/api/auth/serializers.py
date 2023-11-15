from django.conf import settings
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.books.api.serializers import UserSerializer


class AuthTokenSerializer(serializers.Serializer):
    """Custom auth serializer to authenticate email instead of username.

    Copied form rest_framework.authtoken.serializers.AuthTokenSerializer
    """
    email = serializers.CharField(
        write_only=True,
        required=True,
    )
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
        required=True,
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            email=email,
            password=password,
        )

        # The authenticate call simply returns None for is_active=False
        # users. (Assuming the default ModelBackend authentication
        # backend.)
        if not user:
            msg = _("Unable to log in with provided credentials.")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs

    def create(self, validated_data: dict):
        """Escape warning."""

    def update(self, instance, validated_data):
        """Escape warning."""


class TokenSerializer(serializers.Serializer):
    """Auth token for entire app."""
    expiry = serializers.IntegerField(
        help_text=f"Token expires in {settings.REST_KNOX['TOKEN_TTL']}",
    )
    token = serializers.CharField(help_text="Token itself")
    user = UserSerializer()

    def create(self, validated_data):
        """Escape warning."""
        pass

    def update(self, instance, validated_data):
        """Escape warning."""
        pass
