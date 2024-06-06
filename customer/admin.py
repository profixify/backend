from django.contrib import admin
from django.db.models import Value
from django.db.models.functions import Concat

from customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "identity_number", "phone_number")
    search_fields = (
        "identity_number",
        "first_name",
        "last_name",
        "entire_name",
        "phone_number",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(entire_name=Concat("first_name", Value(" "), "last_name"))
        return qs
