from django.urls import path
from apps.books.api.auth.views import LoginView
from knox.views import LogoutView
from apps.books.api.views import StaffCreateView, BookViewSet
from apps.s3upload.api.views import S3PresignedUrlView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("books", BookViewSet, basename="book")

app_name = "api"

urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("staffs/staffs", StaffCreateView.as_view(), name="staff"),
    path(
        "media/s3-presigned-url/",
        S3PresignedUrlView.as_view(),
        name="s3-presigned-url",
    ),
] + router.urls
