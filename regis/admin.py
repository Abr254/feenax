from django.contrib import admin
from django.contrib import admin
from .models import CustomUser
# admin.py
from django.contrib import admin
from .models import Account
# admin.py
from django.contrib import admin
from .models import Account
from django.contrib.auth import get_user_model

# Optionally, register the CustomUser model to show phone number directly from the User model
User = get_user_model()

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'phone_number')  # Add 'phone_number' to list display
    fields = ('user', 'balance')  # You can choose which fields to display in the form
    
    # To show the phone number in the list display, you can add a method:
    def phone_number(self, obj):
        return obj.user.phone_number  # Access the phone number from the related User model
    phone_number.short_description = 'Phone Number'  # Custom label for the column

admin.site.register(Account, AccountAdmin)

# Register your models here.
