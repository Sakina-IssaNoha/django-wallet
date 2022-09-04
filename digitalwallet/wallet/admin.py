from django.contrib import admin 
from ...wallet.models import Currency, Customer, Receipt,Wallet,Account,Transaction,Card,Thirdparty,Notification,Loan,Reward

# Register your models here.
# from .models import Customer, Wallet
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address",)
    search_fields = ("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("origin_country", "amount",)
    search_fields = ("amount","currency",)
admin.site.register(Currency, CurrencyAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ("balance","customer","currency",)
    search_fields = ("balance","customer",)
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_type","account_name", "balance")
    search_fields = ("account_name", "balance")
admin.site.register(Account, AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_amount","transaction_date","origin_account")
    search_fields = ("transaction_amount","transaction_date")
admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ("card_name", "card_number", "card_type","card_status")
    search_fields = ("card_type", "card_name")
admin.site.register(Card, CardAdmin)

class Third_PartyAdmin(admin.ModelAdmin):
    list_display = ("name","thirdparty_id","phone_number","account")
    search_fields = ("name","phone_number")
admin.site.register(Thirdparty, Third_PartyAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("name", "date_and_time","receipt")
    search_fields = ("title", "recepient")
admin.site.register(Notification, NotificationsAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("transaction", "receipt_date", "receipt_type")
    search_fields = ("receipt_date", "transaction")
admin.site.register(Receipt, ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ("loan_type", "amount", "loan_balance")
    search_fields = ("loan_balance", "amount")
admin.site.register(Loan, LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ("transaction", "customer_id", "bonus")
    search_fields = ("transaction", "customer_id")
admin.site.register(Reward, RewardAdmin)


# admin.site.register(Customer,CustomerAdmin) 
# admin.site.register(Wallet)
# admin.site.register(Account)
# admin.site.register(Transaction)
# admin.site.register(Card)
# admin.site.register(Thirdparty)
# admin.site.register(Notification)
# admin.site.register(Loan)
# admin.site.register(Reward)
# admin.site.register(Currency)
# admin.site.register(Receipt)
