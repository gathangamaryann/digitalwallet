from datetime import datetime
from distutils.command.upload import upload
from importlib.util import module_from_spec
from time import time
from django.db import models





# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    adress=models.TextField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    customergender=models.CharField(max_length=10,null=True)
    age=models.CharField(max_length=10)
    profile_picture=models.ImageField(upload_to='profile_picture/',null=True)
class Account(models.Model):   
    account_name=models.CharField(max_length=20)
    account_number=models.CharField(max_length=20)
    account_pin=models.PositiveBigIntegerField()
    account_balance=models.PositiveBigIntegerField()
class Loan(models.Model): 
    amount=models.PositiveBigIntegerField()
    period_of_loan=models.DateTimeFielddefault=datetime.now()
    repayment_reschedules=models.DateTimeField(default=datetime.now)
    loan_id=models.CharField(max_length=20) 
    loan_type=models.CharField(max_length=20) 
class Chatbot(models.Model):
    support_and_agent_rating=models.CharField(max_length=20)
    transcript_emails=models.CharField(max_length=100)
    chat_log=models.CharField(max_length=20)
class Notifications(models.Model):
    user_id=models.PositiveBigIntegerField()
    message= models.CharField(max_length=100)
    transaction_description=models.CharField(max_length=100)
    transaction_id=models.CharField(max_length=20)  
    transaction_amount=models.PositiveBigIntegerField() 
    transaction_number=models.CharField(max_length=100)
class Currency(models.Model):
    country_of_origin=models.CharField(max_length=100) 
    symbol=models.CharField(max_length=100)
    amount=models.PositiveBigIntegerField()  
class Wallet(models.Model):
    balance=models.PositiveBigIntegerField()
    user_id=models.PositiveBigIntegerField() 
    amount=models.PositiveBigIntegerField() 
    time=models.DateTimeField(default=datetime.now)
    status=models.CharField(max_length=100)
    history=models.DateTimeField(default=datetime.now)
class Qr_code(models.Model):
    website_url=models.URLField() 
    contact_details=models.EmailField()   
class Receipt(models.Model):
    receipt_type=models.CharField(max_length=100)   
    receipt_date=models.DateField()
    bill_number=models.PositiveBigIntegerField()
class Reward(models.Model):
    name=models.CharField(max_length=20)   
    customer_id=models.PositiveBigIntegerField() 
class Third_party(models.Model):
    account_name=models.CharField(max_length=20)
    account_number=models.PositiveBigIntegerField()
    amount=models.PositiveBigIntegerField()
    currency=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
class Transaction(models.Model):
    transaction_Code=models.CharField(max_length=20)
    transaction_number=models.CharField(max_length=20)
    transaction_type=models.CharField(max_length=20)
    transaction_charge=models.BigIntegerField
    date_and_time=models.DateTimeField(default=datetime.now)
    wallet=models.ForeignKey(null=True,on_delete=models.CASCADE,to=Wallet)
    receipt=models.OneToOneField(Receipt,on_delete=models.CASCADE,primary_key=True)
    origin_account= models.ForeignKey(Account,on_delete=models.CASCADE,related_name="Transaction_origin_account",null=True)
    destination_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="Transaction_destination_account",null=True)
class Card(models.Model):
    user_Card_number=models.IntegerField()
    pin=models.CharField(max_length=20)
    debit_card=models.CharField(max_length=20)
    credit_card=models.CharField(max_length=20)
    expiry_date=models.DateTimeField(default=datetime.now)
    issued_date=models.DateTimeField(default=datetime.now)
    wallet=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="Card_wallet")
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="Card_account")
    issuer=models.CharField(max_length=20)















   