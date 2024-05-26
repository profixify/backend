from django.contrib import admin

from settings.models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ["default_currency"]
