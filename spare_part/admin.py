from django.contrib import admin

from spare_part.models import Brand, Model, SparePart


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ("name", "price_with_currency", "brand", "model")
    search_fields = ("name", "price")
    readonly_fields = ("left_amount", "temp_amount")
