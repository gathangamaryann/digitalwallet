from django.urls import path

from.import views

urlpatterns=[
    path("register/", views.register_customer, name="registration"),
    path("account/",views. register_account, name="account"),
    path("loan/", views.register_loan, name="loan"),
    path("notification/",views. register_notifications, name="notification"),
    path("currency/", views.register_currency, name="currency"),
    path("wallet/", views.register_wallet, name="wallet"),
    path("receipt/", views.register_receipt, name="receipt"),
    path("reward/", views.register_reward, name="reward"),
    path("transaction/",views. register_transaction, name="transaction"),
    path("card/", views.register_card, name="card"),
    path("customers/",views.list_customer,name="customers"),
    path("accounts/",views.list_account,name="account"),
    path("loans/",views.list_loan,name="loans"),
    path("notifications/",views.list_notification,name="notifications"),
    path("currencies/",views.list_currency,name="curencies"),
    path("wallets/",views.list_wallet,name="wallet"), 
    path("receipts/",views.list_wallet,name="receipts"),
    path("rewards/",views.list_reward,name="rewards"),
    path("transactions/",views.list_transaction,name="transactions"),
    path("cards/",views.list_card,name="cards")
     
   
   
    
    
   
    
   
    
    
    

]