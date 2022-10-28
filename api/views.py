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
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

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



class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)

    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class= TransactionSerilaizers    



class ReceiptsViewSet(viewsets.ModelViewSet):
    queryset=Receipt.objects.all()
    serializer_class= ReceiptSerilaizers    



class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class= LoanSerilaizers         


class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
       message, status = account.deposit(amount)
       return Response(message, status=status)
class AccountWithdrawView(views.APIView):
   """
   This class allows withdraw of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
       message, status = account.withdraw(amount)
       return Response(message, status=status)
class AccountTransferView(views.APIView):
   def post(self, request, format=None):
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
       message, status = account.transfer(amount)
       return Response(message, status=status)
class AccountRequestLoanView(views.APIView):
   def post(self, request, format=None):
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
       message, status = account.request_loan(amount)
       return Response(message, status=status)
class AccountRepayLoanView(views.APIView):
   def post(self, request, format=None):
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
       message, status = account.repay_loan(amount)
       return Response(message, status=status)
class AccountBuyAirtimeView(views.APIView):
   def post(self, request, format=None):
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
       message, status = account.buy_airtime(amount)
       return Response(message, status=status)

class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notifications.objects.all()
    serializer_class= NotificationsSerilaizers       



 