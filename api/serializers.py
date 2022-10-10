from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from wallet.models import Customer, Wallet,Card,Account,Transaction,Notifications,Receipt,Loan

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields= ('first_name', 'last_name', 'email' )


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wallet
        fields= ('balance', 'user_id', 'amount','time','status','history' )



class CardSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('User_card_number', 'debit')       




class AccountSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_number','account_type','balance','name','wallet',)                       





class TransactionSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_ref','wallet','transaction_ref','transaction_type','transaction_charge','transaction_date','original_account','destination_account',)     




class LoanSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('loan_number','loan_type','balance','walllet','intrest_rate','pin','guaranter','due_date','loan_balance','loan_term',)      



class ReceiptSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('receipt_type','receipt_date','recipt_number','recipt_File','transaction','total_Amount','account',)        





class NotificationsSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('notification_Id','date','status','recipient',)           