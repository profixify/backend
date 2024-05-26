from rest_framework import serializers

from customer.models import Customer
from repair.models import Repair
from spare_part.models import SparePart


class DashboardCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "uuid",
            "full_name",
        )


class DashboardSparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePart
        fields = ("uuid", "name")


class DashboardRepairListSerializer(serializers.ModelSerializer):
    customer = DashboardCustomerSerializer(read_only=True)
    spare_part = DashboardSparePartSerializer(read_only=True)

    class Meta:
        model = Repair
        fields = ("uuid", "code", "customer", "spare_part", "status")
