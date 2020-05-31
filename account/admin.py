"""User admin module"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from account.domain.models.custom_user import CustomUser


class CustomUserAdmin(UserAdmin):
    """admin description for CustomUser model"""
    date_hierarchy = 'create_at'

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal Information'),
         {'fields': ('email', 'first_name', 'last_name', 'phone_number')}),
        (_('Permissions'),
         {'fields': ('is_staff', 'is_active', 'is_superuser',)})
    )
    # exclude = ('username',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2')
        }),
        (_('Personal Information'),
         {'fields': ('email', 'first_name', 'last_name', 'phone_number')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'phone_number',
                    'is_staff')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)
