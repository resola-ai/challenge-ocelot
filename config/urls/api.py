from django.conf import settings
from django.urls import include, path
from apps.books.api.auth.views import LoginView
from knox.views import LogoutView
from apps.books.api.views import StaffCreateView, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("books", BookViewSet, basename="book")


urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("staffs/staffs", StaffCreateView.as_view(), name="staff"),
] + router.urls

# Add open_api urls only to not production envs
if settings.DEBUG:
    urlpatterns.append(
        path(
            "api/v1/open-api/", include("config.urls.open_api"),
        ),
    )
