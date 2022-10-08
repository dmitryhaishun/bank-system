from django.db import models
from django.contrib.auth.models import AbstractUser

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

    def get_random_string():
        wallet_names = Wallet.objects.values_list("wallet_name", flat=True)
        while True:
            wallet_name = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if wallet_name not in wallet_names:
                return wallet_name


    wallet_name = models.CharField(max_length=8, default=get_random_string, editable=False, unique=True)
    wallet_type = models.CharField(max_length=10, choices=WALLET_TYPE_CHOICES, default='visa')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EUR')
    balance = models.FloatField(max_length=5, default=0.00, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.wallet_name

class Transaction(models.Model):
    sender = models.ForeignKey(Wallet, to_field='wallet_name', related_name='senders', on_delete=models.CASCADE, )
    receiver = models.ForeignKey(Wallet, to_field='wallet_name', related_name='receivers', on_delete=models.CASCADE)
    transfer_amount = models.FloatField(max_length=5, default=0.00)
    commision = models.FloatField(max_length=100, default=0.1, editable=False)
    status = models.CharField(max_length=10, default='PAID', editable=False)
    timestamp = models.DateTimeField(auto_now=True, null=True)