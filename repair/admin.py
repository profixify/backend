from django.contrib import admin

from repair.models import Repair, RepairStatus


@admin.register(RepairStatus)
class RepairStatusAdmin(admin.ModelAdmin):
    list_display = ("title", "repair", "note", "status")


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "customer",
        "spare_part",
        "sim_lock",
        "phone_lock",
        # "status",
    )
    search_fields = ("code",)
    autocomplete_fields = ["spare_part", "customer"]
