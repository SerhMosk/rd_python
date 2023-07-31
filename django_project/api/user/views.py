from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.user.filters import UserFilter
from api.user.pagination import UserPagination
from user.models import User
from api.user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = UserFilter
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering_fields = ('id', 'age', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
