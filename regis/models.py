from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings 

class CustomUser(AbstractUser):
    # Add any custom fields you want, e.g., phone number
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
# models.py

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.user.username} - Balance: ksh{self.balance}'     