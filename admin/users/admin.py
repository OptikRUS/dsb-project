from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'telegram_id', 'telegram_username', 'phone', 'updated_at', 'created_at')


admin.site.register(Client, ClientAdmin)
