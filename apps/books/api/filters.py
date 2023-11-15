import django_filters
from django.db.models import Q

from apps.books.models import Book


class BookFilter(django_filters.FilterSet):

    author = django_filters.filters.CharFilter(
        method="filter_by_author",
    )

    class Meta:
        model = Book
        fields = (
            "author",
            "genre",
        )

    @staticmethod
    def filter_by_author(queryset, name, value):
        """Filter books based on both author's first_name and last_name"""
        return queryset.filter(
            Q(author__first_name__icontains=value) |
            Q(author__last_name__icontains=value),
        )
