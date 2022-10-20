from django.urls import path
from . import views


urlpatterns = [
    path("wallets/", views.WalletListCreate.as_view(), name="wallets-list"),
    path("wallets/transactions/", views.TransactionListCreate.as_view(), name="wallets-transactions",),
    path("wallets/<wallet_name>/", views.WalletDetailView.as_view(), name="wallet-detail"),
    path("wallets/transactions/<int:id>/", views.TransactionDetailView.as_view(), name="transaction",),
    path("wallets/transactions/<wallet_name>/", views.TransactionListView.as_view(), name="wallet-transactions",),
    path("register/", views.CreateUserView.as_view(), name="register"),
]
