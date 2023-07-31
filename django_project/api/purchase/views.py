from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from api.purchase.filters import PurchaseFilter
from api.purchase.serializers import PurchaseSerializer
from purchase.models import Purchase


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = PurchaseFilter
    search_fields = ('id',)
    ordering_fields = ('id', 'book_id', 'user_id', 'created_at')
