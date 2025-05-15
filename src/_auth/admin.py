from django.contrib import admin
from .models import User, CheckPhone

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", 'first_name', 'last_name', 'phone_number')


@admin.register(CheckPhone)
class CheckPhoneAdmin(admin.ModelAdmin):
    list_display = ("code", "user")
