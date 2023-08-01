import django_filters

from user.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
            'email': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'age': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
            'date_joined': ['exact', 'gt', 'lt', 'gte', 'lte', 'contains'],
        }
