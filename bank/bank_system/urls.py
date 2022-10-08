from django.urls import path
from . import views

urlpatterns = [
    path('wallets/', views.WalletListCreate.as_view()),
    #path('wallets/<wallet_name>/', views.WalletDetailView.as_view()),
    path('wallets/transactions/', views.TransactionListCreate.as_view()),
    path('wallets/transactions/<int:id>/', views.TransactionDetailView.as_view()),
    path('wallets/transactions/<wallet_name>/', views.TransactionListView.as_view())

]