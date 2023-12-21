from django.contrib import admin
from .models import Service, Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "place")


admin.site.register(Service, ServiceAdmin)
admin.site.register(Place, PlaceAdmin)
