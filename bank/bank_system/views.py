from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .models import Wallet
from .serializers import WalletSerializer
from rest_framework import generics

class WalletListCreate(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticatedOrReadOnly)

class WalletDetailView(generics.RetrieveDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = 'wallet_name'
    permission_classes = (IsAuthenticated)
