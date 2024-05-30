from django.contrib import admin

from spare_part.models import SparePart


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ("name", "price_with_currency")
    search_fields = ("name", "price")
