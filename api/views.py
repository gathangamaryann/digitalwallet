import sre_compile
from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Customer, Wallet,Account,Card,Transaction,Loan,Receipt,Notifications
from .serializers import CardSerilaizers, CustomerSerializer, NotificationsSerilaizers, ReceiptSerilaizers
from .serializers import WalletSerializer
from .serializers import TransactionSerilaizers
from.serializers import AccountSerilaizers
from .serializers import CardSerilaizers
from.serializers import LoanSerilaizers
# Create your views here.
                     


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset =Wallet.objects.all()
    serializer_class = WalletSerializer 

     


class CardViewSet(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class= CardSerilaizers   



class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerilaizers



class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerilaizers 



class ReceiptsViewSet(viewsets.ModelViewSet):
    queryset=Receipt.objects.all()
    serializer_class= ReceiptSerilaizers    



class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=LoanSerilaizers       



class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notifications.objects.all()
    serializer_class= NotificationsSerilaizers      
