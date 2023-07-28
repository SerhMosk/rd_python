from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField(min_value=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'age', 'date_joined', 'is_superuser', 'is_staff', 'is_active')
        read_only_fields = ('date_joined',)

    def validate_username(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Username is too short')
        return value

    def validate_age(self, value):
        if value < 6:
            raise serializers.ValidationError('Age is too small')
        return value
