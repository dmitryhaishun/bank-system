from rest_framework import serializers
from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Wallet
        exclude = []