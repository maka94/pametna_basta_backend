from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model

User = get_user_model()

class InputRegisterUserSerializer(serializers.Serializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise exceptions.ValidationError('Username already taken')
        else:
            return value

class OutputRegisterUserSerializer(serializers.Serializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    id = serializers.IntegerField()

class InputLoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
