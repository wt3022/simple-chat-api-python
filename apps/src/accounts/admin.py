from allauth.account.models import EmailAddress
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm as DefaultUserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import User


class UserChangeForm(DefaultUserChangeForm):
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            return email

        if (
            User.objects.filter(email=email).exclude(id=self.instance.id).exists()
            or EmailAddress.objects.filter(email=email).exclude(user_id=self.instance.id).exists()
        ):
            raise forms.ValidationError("このメールアドレスはすでに使用されています")
        return email


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )


admin.site.register(User, CustomUserAdmin)
