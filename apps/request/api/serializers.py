from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers

class MyTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['access'] = str(refresh.access_token)
        return data


class RequestSerializer(serializers.Serializer):

    frase_enviada = serializers.CharField(max_length=999)
    conversation_id = serializers.UUIDField(format='hex_verbose')
    site_id = serializers.CharField(max_length=10)
    bot_name = serializers.CharField(max_length=100)