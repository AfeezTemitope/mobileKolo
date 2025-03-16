from django.contrib import admin
from .models import Wallet, User


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['account_number']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'email', 'wallet']
    search_fields = ['username', 'email']
    list_filter = ['is_staff', 'is_active']
