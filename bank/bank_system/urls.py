from django.urls import path
from . import views
# TODO: РЕШИТЬ ПРОБЛЕМУ С СОВПАДЕНИЯМИ ЮРЛОВ 2/3
urlpatterns = [
    path('wallets/', views.WalletListCreate.as_view()),
    # path('wallets/<wallet_name>/', views.WalletDetailView.as_view()),
    path('wallets/transactions/', views.TransactionListCreate.as_view()),
    path('wallets/transactions/<transaction_id>/', views.TransactionDetailView.as_view()),
    path('wallets/transactions/<wallet_name>/', views.TransactionListView.as_view()),
    path('register/', views.CreateUserView.as_view()),
]