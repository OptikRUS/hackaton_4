from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("__str__", "role", "last_login")
    exclude = ("groups", "user_permissions", "password")
