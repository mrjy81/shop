from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
import django_jalali.admin as jadmin
from django_jalali.admin.filters import JDateFieldListFilter


class CustomUserAdmin(UserAdmin):
    fieldsets = [
        *UserAdmin.fieldsets,
        (
            'Additional fields',
            {
                'fields': (
                    'age',
                )
            }
        )
    ]


admin.site.register(Account, CustomUserAdmin)
