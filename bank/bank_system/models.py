from django.db import models
from django.contrib.auth.models import AbstractUser

import string
import random

class CustomUser(models.Model):
    pass

#TODO:
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

    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE)
    wallet_name = models.CharField(max_length=8, default=get_random_string, editable=False, unique=True)
    wallet_type = models.CharField(max_length=10, choices=WALLET_TYPE_CHOICES, default='visa')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EUR')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    balance = 0.00


class Transaction(models.Model):
    pass