from django.contrib.auth import login
from drf_spectacular.utils import extend_schema
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions

from . import serializers


class LoginView(KnoxLoginView):
    """Token-based Auth view."""

    permission_classes = (permissions.AllowAny,)

    @extend_schema(
        request=serializers.AuthTokenSerializer,
        responses=serializers.TokenSerializer,
    )
    def post(self, request, *args, **kwargs):
        """Login user and get auth token with expiry."""
        serializer = serializers.AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request, serializer.validated_data["user"])
        return super().post(request, format=None)
