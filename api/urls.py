from django.urls import path,include
from rest_framework import routers
from .views import AccountDepositView, CustomerViewSet
from .views import WalletViewSet
from .views import CardViewSet
from .views import AccountViewSet
from .views import NotificationViewSet
from .views import TransactionViewSet
from .views import ReceiptsViewSet
from .views import LoanViewSet 
from . import views 
  

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'cards',CardViewSet)
router.register(r'accounts',AccountViewSet)
router.register(r'notifications',NotificationViewSet)
router.register(r'transactions',TransactionViewSet)
router.register(r'loan',LoanViewSet)
router.register(r'receipt',ReceiptsViewSet)


urlpatterns=[
    path('', include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("withdraw/", views.AccountWithdrawView.as_view(), name="withdraw-view"),
    path("transfer/", views.AccountTransferView.as_view(), name="transfer-view"),
    path("request_loan/", views.AccountRequestLoanView.as_view(), name="request-loan-view"),
    path("repay_loan/", views.AccountRepayLoanView.as_view(), name="repay-loan-view"),
    path("buy_airtime/", views.AccountBuyAirtimeView.as_view(), name="buy-airtime-view"),
]


