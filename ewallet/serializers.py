from djoser.serializers import UserCreateSerializer
from ewallet.models import Wallet
from rest_framework import serializers
from django.contrib.auth import get_user_model


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['account_number']


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password']
