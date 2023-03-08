from rest_framework import serializers
from .model import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'token'
        ]
        read_only_fields = ['token']