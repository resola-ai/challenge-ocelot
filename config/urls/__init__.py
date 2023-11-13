from django.contrib import admin
from django.urls import include, path
from .api import urlpatterns as api_urlpatterns

urlpatterns = [
    path("mission-control-center/", admin.site.urls),
]

urlpatterns += api_urlpatterns
