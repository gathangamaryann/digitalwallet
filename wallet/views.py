from locale import currency
import re
from urllib import request
from django.shortcuts import redirect, render
from wallet .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, Transaction, Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
def register_customer(request):
    if request.method=="POST":
     form=CustomerRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})




def list_customer(request):
    customers=Customer.objects.all ()   
    return render(request,"wallet/list_customer.html",{"customers":customers})
    


def register_account(request):
     if request.method=="POST":
      form=AccountRegistrationForm(request.POST)
      if form.is_valid():
        form.save()
     else:
        form=AccountRegistrationForm()
     return render(request,"wallet/register_account.html",{"form":form}) 
def list_account(request):
    accounts=Account.objects.all()
    return render(request,"wallet/list_account.html",{"accounts":accounts})


def register_loan(request):
    if request.method=="POST":
     form=LoanRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})  
def list_loan(request):
    loan=Loan.objects.all()
    return render(request,"wallet/list_loan.html",{"loan":loan})



def register_notifications(request):
    if request.method=="POST":
     form=NotificationsRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=NotificationsRegistrationForm()
    return render(request,"wallet/register_notifications.html",{"form":form})  
def list_notification(request):
    notification=Notifications.objects.all()
    return render(request,"wallet/list_notification.html",{"notification":notification})


def register_currency(request):
    if request.method=="POST":
     form=CurrencyRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form})  
def list_currency(request):
    currencies=Currency.objects.all()
    return render(request,"wallet/list_currency.html",{"currency":currencies})




def register_wallet(request):
    if request.method=="POST":
     form=WalletRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
       form=WalletRegistrationForm ()
    return render(request,"wallet/register_currency.html",{"form":form})  
def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet/list_wallet.html",{"wallet":wallets})




def register_receipt(request):
    if request.method=="POST":
      form=ReceiptRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form":form})  
def list_receipt(request):
    receipts=Receipt.objects.all()
    return render(request,"wallet/list_receipt.html",{"receipt":receipts})




def  register_reward(request):
    if request.method=="POST":
      form=RewardRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
         form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})  
def list_reward(request):
    rewards=Reward.objects.all()
    return render(request,"wallet/list_reward.html",{"reward":rewards})




def  register_transaction(request):
    if request.method=="POST":
     form=TransactionRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})  
def list_transaction(request):
    transaction=Transaction.objects.all()
    return render(request,"wallet/list_transaction.html",{"transact":transaction})




def register_card(request):
    if request.method=="POST":
     form=CardRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
         form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})  
def list_card(request):
    card=Card.objects.all()
    return render(request,"wallet/list_currency.html",{"cards":card})

def customer_profile(request,id):
    customer=Customer.objects.get(id=id)   
    return render(request,"wallet/customer_profile.html",{"customers":customer})   

def edit_customer(request,id):
    customer=Customer.objects.get(id=id)  
    request.method='POST'
    form=CustomerRegistrationForm(request.POST,instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_profile',id=customer.id)
    else:
     form=CustomerRegistrationForm(instance=customer)
     return render(request,"wallet/edit_customer.html",{'form':form})

def wallet_profile(request, id):
    wallet=Wallet.objects.get(id=id)
    return render(request,"wallet/wallet_profile.html",{"wallet":wallet})

def edit_wallet(request, id):
    wallet=Wallet.objects.get(id=id)  
    request.method='POST'
    form=WalletRegistrationForm(request.POST,instance=wallet)
    if form.is_valid():
        form.save()
        return redirect('wallet/edit_wallet.html',{'form':form})


def  account_profile(request, id):
    Account=Account.objects.get(id=id)
    return render(request,"wallet/account_profile.html",{"accounts":Account})

def edit_account(request, id):
    accounts=Account .objects.get(id=id)  
    request.method='POST'
    form=AccountRegistrationForm(request.POST,instance=accounts)
    if form.is_valid():
        form.save()
        return redirect('wallet/edit_account.html',{'form':form}
         )

def  card_profile(request, id):
    Card=Card.objects.get(id=id)
    return render(request,"wallet/card_profile.html",{"card":Card})

def edit_card(request, id):
    card=Card .objects.get(id=id)  
    request.method='POST'
    form=CardRegistrationForm(request.POST,instance=card)
    if form.is_valid():
        form.save()
        return redirect('wallet/edit_card.html',{'form':form})

def  transaction_profile(request, id):
    transaction=Transaction.objects.get(id=id)
    return render(request,"wallet/transaction_profile.html",{"transact":transaction})

def edit_transaction(request, id):
    transaction=Transaction .objects.get(id=id)  
    request.method='POST'
    form=TransactionRegistrationForm(request.POST,instance=transaction)
    if form.is_valid():
        form.save()
        return redirect('wallet/edit_transaction.html',{'form':form})

def  receipt_profile(request, id):
    receipts=Receipt.objects.get(id=id)
    return render(request,"wallet/receipt_profile.html",{"receipt":receipts})

def edit_receipt(request, id):
    receipts=Receipt .objects.get(id=id)  
    request.method='POST'
    form=ReceiptRegistrationForm(request.POST,instance=receipts)
    if form.is_valid():
        form.save()
        return redirect('wallet/edit_receipt.html',{'form':form})
                                                         