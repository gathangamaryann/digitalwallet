import email
from locale import currency
from django.contrib import admin 




from.models import Account, Card, Chatbot, Currency, Customer, Loan, Notifications, Qr_code, Receipt, Reward, Third_party, Transaction, Wallet



# # Register your models here.
# class CustomerAdmin(admin.ModelAdmin):
#   list_display=('first_name','Last_name','age','email',)
#   search_field=('first_name','last_name')

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(Chatbot)
admin.site.register(Notifications)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Qr_code)
admin.site.register(Receipt)
admin.site.register(Reward)
admin.site.register(Third_party)
admin.site.register(Transaction)
admin.site.register(Card)