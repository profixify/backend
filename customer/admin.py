from django.contrib import admin
from django.db.models import Value
from django.db.models.functions import Concat

from customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number")
    search_fields = (
        "first_name",
        "last_name",
        "entire_name",
        "phone_number",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(entire_name=Concat("first_name", Value(" "), "last_name"))
        return qs
