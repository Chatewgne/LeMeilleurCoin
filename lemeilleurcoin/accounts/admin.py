# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Overwritte user creation form in admin page to include phone number in Users
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "username",
        "phone_number",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "username",
        "phone_number",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "phone_number", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = (
        "username",
        "phone_number",
    )
    ordering = (
        "username",
        "phone_number",
    )


# Register new form to admin page
admin.site.register(CustomUser, CustomUserAdmin)
