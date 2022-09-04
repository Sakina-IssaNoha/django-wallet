import imp
from django.urls import path 
from .views import register_currency, register_customer, register_transaction
from .views import register_wallet
from .views import register_currency
from .views import register_account
from .views import register_transaction
from .views import register_card
from .views import register_thirdparty
from .views import register_notification
from .views import register_receipt
from .views import register_loan
from .views import register_reward

urlpatterns = [
    path("register/",register_customer,name="registation"),
    path("wallet/",register_wallet,name="registation"),
    path("currency/",register_currency,name="registation"),
    path("account/",register_account,name="registation"),
    path("transaction/",register_transaction,name="registation"),
    path("card/",register_card,name="registation"),
    path("thirdparty/",register_thirdparty,name="registation"),
    path("notification/",register_notification,name="registation"),
    path("receipt/",register_receipt,name="registation"),
    path("loan/",register_loan,name="registation"),
    path("reward/",register_reward,name="registation"),

]
