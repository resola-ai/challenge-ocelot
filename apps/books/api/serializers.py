from django.db import transaction
from rest_framework import serializers

from apps.books.models import Author, Book, BookCover, User
from apps.core.serializers import NestedCreateUpdateMixin
from apps.s3upload.api.serializers import S3DirectUploadURLField


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = (
            "last_login",
        )

    def create(self, validated_data):
        # Check if 'password' is present in the data
        if 'password' in validated_data:
            # Get the password and remove it from validated_data
            password = validated_data.pop('password')
            # Create the user without setting the password initially
            user = User.objects.create(**validated_data)
            # Set the password using the set_password method
            user.set_password(password)
            user.save()
            return user
        else:
            # Handle the case if 'password' is not present in the request data
            raise serializers.ValidationError("Password field is required")


class StaffSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        required=False,
        allow_null=True,
        write_only=True,
        style={'input_type': 'password'},
    )
    has_usable_password = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'new_password',  # Let's skip password double check
            'has_usable_password',
        )

    @transaction.atomic
    def create(self, validated_data):
        """Create user with usable password.

        In practice, we may go for email verification workflow
        for user registration.
        But for simplicity, let's skip it at the moment.
        """
        new_password = validated_data.pop('new_password', False)
        instance = super().create(validated_data)

        if new_password:
            instance.set_password(new_password)
            instance.save()
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password', False)
        if new_password:
            instance.set_password(new_password)
        if new_password is None:
            instance.set_unusable_password()
        super().update(instance, validated_data)
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
        )


class BookCoverSerializer(serializers.ModelSerializer):
    file = S3DirectUploadURLField()

    class Meta:
        model = BookCover
        fields = (
            "file",
        )


class BookSerializer(NestedCreateUpdateMixin, serializers.ModelSerializer):
    author = AuthorSerializer(required=False, allow_null=True)
    book_covers = BookCoverSerializer(many=True, required=False)

    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            "publish_date": {"required": False},
            "isbn": {"required": False},
        }
