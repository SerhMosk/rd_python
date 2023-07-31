import django_filters

from purchase.models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'book__id': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
            'book__title': ['icontains'],
            'book__author': ['icontains'],
            'user__id': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
            'user__username': ['icontains'],
            'user__email': ['icontains'],
            'user__first_name': ['icontains'],
            'user__last_name': ['icontains'],
            'user__age': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
            'user__date_joined': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
            'created_at': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
        }
