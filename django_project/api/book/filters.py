import django_filters

from book.models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'author': ['icontains'],
            'year': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
            'price': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
        }
