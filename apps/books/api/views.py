from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.books.models import Book, User
from apps.core.serializers import ActionPermissionMixin

from . import serializers


class StaffCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = serializers.StaffSerializer


class BookViewSet(ActionPermissionMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    action_permission_classes = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAuthenticated],
        "update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
    }
