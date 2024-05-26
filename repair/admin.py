from django.contrib import admin

from repair.models import Repair


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "customer",
        "spare_part",
        "sim_lock",
        "phone_lock",
        "status",
    )
