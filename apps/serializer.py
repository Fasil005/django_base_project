from rest_framework import serializers
from .models import AdminTable


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminTable
        fields = '__all__'

    def create(self, validated_data):
        return AdminTable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.status = validated_data.get('name', instance.status)
        instance.save()
        return instance
