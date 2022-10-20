from rest_framework import serializers
from .models import Wallet, Transaction
from django.contrib.auth import get_user_model

from decimal import Decimal

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "password",
        )


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = []

    def create(self, validated_data):
        if validated_data["currency"] == "EUR" or validated_data["currency"] == "USD":
            validated_data["balance"] = 3.00
        elif validated_data["currency"] == "RUB":
            validated_data["balance"] = 100.00
        return Wallet.objects.create(**validated_data)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = []

    def create(self, validated_data):
        if (
            Wallet.objects.filter(wallet_name=validated_data["sender"]).values()[0][
                "currency"
            ]
            != Wallet.objects.filter(wallet_name=validated_data["receiver"]).values()[
                0
            ]["currency"]
        ):
            validated_data["status"] = "FAILED"
            if validated_data["sender"] == validated_data["receiver"]:
                validated_data["commision"] = Decimal("0.00")
            else:
                validated_data["commision"] = validated_data[
                    "transfer_amount"
                ] * Decimal("0.10")
        elif (
            validated_data["transfer_amount"]
            > Wallet.objects.filter(wallet_name=validated_data["sender"]).values()[0][
                "balance"
            ]
        ):
            validated_data["status"] = "FAILED"
            if validated_data["sender"] == validated_data["receiver"]:
                validated_data["commision"] = Decimal("0.00")
            else:
                validated_data["commision"] = validated_data[
                    "transfer_amount"
                ] * Decimal("0.10")
        else:
            if validated_data["sender"] == validated_data["receiver"]:
                validated_data["commision"] = Decimal("0.00")
                Wallet.objects.filter(wallet_name=validated_data["sender"]).update(
                    balance=(
                        Wallet.objects.filter(
                            wallet_name=validated_data["sender"]
                        ).values()[0]["balance"]
                        - validated_data["transfer_amount"]
                    )
                )
                Wallet.objects.filter(wallet_name=validated_data["receiver"]).update(
                    balance=(
                        Wallet.objects.filter(
                            wallet_name=validated_data["receiver"]
                        ).values()[0]["balance"]
                        + validated_data["transfer_amount"]
                    )
                )
            else:
                validated_data["commision"] = validated_data[
                    "transfer_amount"
                ] * Decimal("0.10")
                Wallet.objects.filter(wallet_name=validated_data["sender"]).update(
                    balance=(
                        Decimal(
                            Wallet.objects.filter(
                                wallet_name=validated_data["sender"]
                            ).values()[0]["balance"]
                        )
                        - validated_data["transfer_amount"]
                    )
                )
                Wallet.objects.filter(wallet_name=validated_data["receiver"]).update(
                    balance=(
                        Decimal(
                            Wallet.objects.filter(
                                wallet_name=validated_data["receiver"]
                            ).values()[0]["balance"]
                        )
                        + validated_data["transfer_amount"]
                        - validated_data["commision"]
                    )
                )
        return Transaction.objects.create(**validated_data)
