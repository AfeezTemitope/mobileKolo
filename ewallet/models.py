from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Wallet(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, nullable=False)


class User(AbstractUser):
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE, related_name='user')

