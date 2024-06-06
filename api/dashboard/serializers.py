from rest_framework import serializers

from api.repair.serializers import RepairStatusSerializer
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
    latest_status = serializers.SerializerMethodField()

    class Meta:
        model = Repair
        fields = ("uuid", "code", "customer", "spare_part", "latest_status")

    def get_latest_status(self, obj):
        latest_status = obj.statuses.order_by("-created_at").first()
        if latest_status:
            return RepairStatusSerializer(latest_status).data["status"]
        return None
