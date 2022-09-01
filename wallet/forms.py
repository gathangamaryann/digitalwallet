
from .models import Account, Customer
from django import forms
from django.forms import ModelForm

class CustomerRegistrationForm(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
class AccountRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"        
class LoanRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"        
class NotificationsRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"        
class CurrencyRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"        
class WalletRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__" 
class ReceiptRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"        
class RewardRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"        
class TransactionRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"        
class CardRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"        
                               
                          
      