from rest_framework import serializers
from .models import UserTable


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserTable(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        user.save()
        return user
