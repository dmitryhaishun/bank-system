from rest_framework import serializers
from .models import Wallet, Transaction
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = []

    def create(self, validated_data):
        if validated_data['currency'] == 'EUR' or validated_data['currency'] == 'USD':
            validated_data['balance'] = 3.00
        elif validated_data['currency'] == 'RUB':
            validated_data['balance'] = 100.00
        return Wallet.objects.create(**validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = []

    def create(self, validated_data):
        if validated_data['sender'] == validated_data['receiver']:
            validated_data['commision'] = 0.00
        else:
            validated_data['commision'] = validated_data['transfer_amount'] * 0.1
            #TODO: дописать чтобы был перелив денег
        return Transaction.objects.create(**validated_data)
