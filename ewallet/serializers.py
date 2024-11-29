from djoser.serializers import UserCreateSerializer

from ewallet.models import Wallet, User
from rest_framework import serializers


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'phone_number']


class CustomUserCreateSerializer(UserCreateSerializer):
    wallet = WalletSerializer()

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email', 'password', 'wallet']
