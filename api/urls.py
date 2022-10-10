from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet
from .views import WalletViewSet
from .views import CardViewSet
from .views import AccountViewSet
from .views import NotificationViewSet
from .views import TransactionViewSet
from .views import ReceiptsViewSet
from .views import LoanViewSet    

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
]


