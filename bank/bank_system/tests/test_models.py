from unittest import mock

from django.test import TestCase
import unittest
from ..models import Wallet, CustomUser, Transaction


class WalletModelTest(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create(username="1", password="1")
        user2 = CustomUser.objects.create(username="2", password="2")
        Wallet.objects.create(user=user1, wallet_type="visa", currency="EUR")
        Wallet.objects.create(user=user2, wallet_type="mastercard", currency="RUB")

    def test_wallets_type(self):
        wallet1 = Wallet.objects.all()[0]
        wallet2 = Wallet.objects.all()[1]

        self.assertEqual(wallet1.wallet_type, "visa")
        self.assertEqual(wallet2.wallet_type, "mastercard")

    def test_wallets_currencies(self):
        wallet1 = Wallet.objects.all()[0]
        wallet2 = Wallet.objects.all()[1]

        self.assertEqual(wallet1.currency, "EUR")
        self.assertEqual(wallet2.currency, "RUB")

    def test_wallets_users(self):
        wallet1 = Wallet.objects.all()[0]
        wallet2 = Wallet.objects.all()[1]

        self.assertEqual(wallet1.user_id, 1)
        self.assertEqual(wallet2.user_id, 2)

    def test_unique_wallets_names(self):
        wallet1 = Wallet.objects.all()[0]
        wallet2 = Wallet.objects.all()[1]

        self.assertNotEqual(wallet1.wallet_name, wallet2.wallet_name)


class TransactionWalletTest(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create(username="1", password="1")
        user2 = CustomUser.objects.create(username="2", password="2")
        wallet1 = Wallet.objects.create(user=user1, wallet_type="visa", currency="EUR")
        wallet2 = Wallet.objects.create(
            user=user2, wallet_type="mastercard", currency="RUB"
        )
        wallet3 = Wallet.objects.create(user=user1, wallet_type="visa", currency="RUB")
        Transaction.objects.create(sender=wallet1, receiver=wallet2, transfer_amount=1)
        Transaction.objects.create(sender=wallet2, receiver=wallet3, transfer_amount=1)
        Transaction.objects.create(sender=wallet3, receiver=wallet2, transfer_amount=1)

    def test_transactions_senders(self):
        transaction1 = Transaction.objects.all()[0]
        transaction2 = Transaction.objects.all()[1]
        transaction3 = Transaction.objects.all()[2]

        self.assertEqual(transaction1.sender, Wallet.objects.all()[0])
        self.assertEqual(transaction2.sender, Wallet.objects.all()[1])
        self.assertEqual(transaction3.sender, Wallet.objects.all()[2])

    def test_transactions_receivers(self):
        transaction1 = Transaction.objects.all()[0]
        transaction2 = Transaction.objects.all()[1]
        transaction3 = Transaction.objects.all()[2]

        self.assertEqual(transaction1.receiver, Wallet.objects.all()[1])
        self.assertEqual(transaction2.receiver, Wallet.objects.all()[2])
        self.assertEqual(transaction3.receiver, Wallet.objects.all()[1])


class CustomUserTest(TestCase):
    def setUp(self):
        CustomUser.objects.create(username="1", password="111")
        CustomUser.objects.create(username="2", password="QWE")
        CustomUser.objects.create(username="3", password="ASD")

    def test_users_id(self):
        user1 = CustomUser.objects.all()[0]
        user2 = CustomUser.objects.all()[1]
        user3 = CustomUser.objects.all()[2]

        self.assertEqual(user1.id, 1)
        self.assertEqual(user2.id, 2)
        self.assertEqual(user3.id, 3)

    def test_users_passwords(self):
        user1 = CustomUser.objects.all()[0]
        user2 = CustomUser.objects.all()[1]
        user3 = CustomUser.objects.all()[2]

        self.assertEqual(user1.username, "1")
        self.assertEqual(user2.username, "2")
        self.assertEqual(user3.username, "3")

    def test_users_passwords(self):
        user1 = CustomUser.objects.all()[0]
        user2 = CustomUser.objects.all()[1]
        user3 = CustomUser.objects.all()[2]

        self.assertEqual(user1.password, "111")
        self.assertEqual(user2.password, "QWE")
        self.assertEqual(user3.password, "ASD")


if __name__ == "__main__":
    unittest.main()
