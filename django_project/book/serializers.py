from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    author = serializers.CharField()
    year = serializers.IntegerField(min_value=1)
    price = serializers.IntegerField(min_value=1)

    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'price')

    def validate_year(self, value):
        if value < 1:
            raise serializers.ValidationError('Year is too small')
        return value

    def validate_price(self, value):
        if value < 1:
            raise serializers.ValidationError('Price is too small')
        return value
