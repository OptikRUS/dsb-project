from django.contrib import admin
from .models import Slot, Ticket


class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot_date', 'slot_time', 'is_open')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('client', 'slot', 'service', 'updated_at', 'created_at', 'is_active')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Slot, SlotAdmin)
