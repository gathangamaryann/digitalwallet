import email
from locale import currency
from django.contrib import admin 




from.models import Account, Card, Chatbot, Currency, Customer, Loan, Notifications, Qr_code, Receipt, Reward, Third_party, Transaction, Wallet



# # Register your models here.
# class CustomerAdmin(admin.ModelAdmin):
#   list_display=('first_name','Last_name','age','email',)
#   search_field=('first_name','last_name')
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields = ('first_name', 'last_name',)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name','account_number','account_pin',)
    search_fields = ('account_name', 'account_number',)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('amount','period_of_loan','loan_id','loan_type',)
    search_fields = ('loan_type', 'period_of_name',)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('user_id',)
    search_fields = ('user_id', )
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country_of_origin','symbol','amount')
    search_fields = ('country_of_origin', 'symbol',)  
class WalletAdmin(admin.ModelAdmin):
    list_display = ('balance','user_id','amount','time','status','history')
    search_fields = ('status', 'user_id',)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_type','bill_number')
    search_fields = ('receipt_type',)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('name','customer_id')
    search_fields = ('name', 'customer_id',)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_Code','transaction_number','transaction_type','transaction_charge','date_and_time')
    search_fields = ('first_name', 'last_name',)
class CardAdmin(admin.ModelAdmin):
    list_display = ('pin','expiry_date',)
    search_fields = ('user_Card_number', 'expiry_date',)                 

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Chatbot)
admin.site.register(Notifications,NotificationsAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Qr_code)
admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(Reward,RewardAdmin)
admin.site.register(Third_party)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)