# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'role', 'organization')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'organization')}),
    )

# Note: No 'username' field is set and will be set for the CustomUser model.

admin.site.register(CustomUser, CustomUserAdmin)
