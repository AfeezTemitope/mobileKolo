from random import randint
from django.db import models
from django.contrib.auth.models import AbstractUser


def generate_account_number():
    while True:
        account_number = '22' + ''.join(str(randint(10000000, 99999999)))
        if not Wallet.objects.filter(account_number=account_number).exists():
            return account_number


class Wallet(models.Model):
    account_number = models.CharField(max_length=10, unique=True, blank=False, default=generate_account_number)
    balance = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    pin = models.CharField(max_length=4, default="0000")
    user = models.OneToOneField('User', on_delete=models.PROTECT, related_name='wallet')

    def __str__(self):
        return f"Account: {self.account_number} and {self.balance}"


class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.username
