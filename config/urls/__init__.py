from django.contrib import admin
from django.urls import path
from .api_versions import urlpatterns as api_urlpatterns
from apps.books.views import BookListView

urlpatterns = [
    path("mission-control-center/", admin.site.urls),
    path('books/list-book/', BookListView.as_view(), name='book_list'),
]

urlpatterns += api_urlpatterns
