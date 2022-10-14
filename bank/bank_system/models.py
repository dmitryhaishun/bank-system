from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import string
import random


class CustomUser(AbstractUser):
    pass

class Wallet(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
    )
    WALLET_TYPE_CHOICES = (
        ('visa', 'Visa'),
        ('mastercard', 'MasterCard')
    )
    # def clean(self, request):
    #     from django.core.exceptions import ValidationError
    #     if Wallet.objects.filter(user=self.request.user) > 5:
    #         raise ValidationError('You have reached the maximum number of wallets.')

    def get_random_string():
        wallet_names = Wallet.objects.values_list("wallet_name", flat=True)
        while True:
            wallet_name = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if wallet_name not in wallet_names:
                return wallet_name

    user = models.ForeignKey(CustomUser, to_field='id', on_delete=models.CASCADE, editable=False)
    wallet_name = models.CharField(max_length=8, default=get_random_string, editable=False, unique=True)
    wallet_type = models.CharField(max_length=10, choices=WALLET_TYPE_CHOICES, default='visa')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EUR')
    balance = models.FloatField(max_length=5, default=0.00, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.wallet_name

class Transaction(models.Model):

    def validate_transfer_amount(value):
        if value != '':
            return value
        else:
            raise ValidationError("Enter a correct transfer amount")

    sender = models.ForeignKey(Wallet, to_field='wallet_name', related_name='senders', on_delete=models.CASCADE,)
    receiver = models.ForeignKey(Wallet, to_field='wallet_name', related_name='receivers', on_delete=models.CASCADE)
    transfer_amount = models.FloatField(max_length=5, default=0.00, blank=False, validators=[validate_transfer_amount])
    commision = models.FloatField(max_length=100, default=0.1, editable=False)
    status = models.CharField(max_length=10, default='PAID', editable=False)
    timestamp = models.DateTimeField(auto_now=True, null=True)