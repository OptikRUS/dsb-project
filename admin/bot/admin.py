from django.contrib import admin
from .models import Settings, Button, Page, PagesButtons


admin.site.register(Settings)
admin.site.register(Button)
admin.site.register(Page)
admin.site.register(PagesButtons)
