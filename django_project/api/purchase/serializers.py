from rest_framework import serializers

from api.book.serializers import BookSerializer
from api.user.serializers import UserSerializer
from purchase.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = Purchase
        fields = ('book', 'user', 'created_at')
        read_only_fields = ('created_at',)
