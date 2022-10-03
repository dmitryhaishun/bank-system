from django.urls import path
from . import views

urlpatterns = [
    path('wallets/', views.WalletListCreate.as_view()),
    path('wallets/<wallet_name>/', views.WalletDetailView.as_view()),
    # path('/wallets/transactions/', ),
    # path('/wallets/transactions/<transaction_id>/', ),
    # path('/wallets/transactions/<wallet_name>/', )
]