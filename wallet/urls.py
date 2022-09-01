from django.urls import path
from .views import register_account, register_card, register_currency, register_customer, register_loan, register_notifications, register_receipt, register_reward, register_transaction, register_wallet

urlpatterns=[
    path("register/", register_customer, name="registration"),
    path("account/", register_account, name="account"),
    path("loan/", register_loan, name="loan"),
    path("notification/", register_notifications, name="notification"),
    path("currency/", register_currency, name="currency"),
    path("wallet/", register_wallet, name="wallet"),
    path("receipt/", register_receipt, name="receipt"),
    path("reward/", register_reward, name="reward"),
    path("transaction/", register_transaction, name="transaction"),
    path("card/", register_card, name="card"),
    
    

]