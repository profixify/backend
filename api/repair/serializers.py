from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.customer.serializers import CustomerSerializer
from api.spare_part.serializers import SparePartSerializer
from customer.models import Customer
from repair.models import Repair, RepairStatus
from spare_part.models import SparePart


class RepairStatusSerializer(ModelSerializer):
    class Meta:
        model = RepairStatus
        fields = ("uuid", "title", "note", "status", "created_at", "updated_at")


class RepairReadSerializer(ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    spare_part = SparePartSerializer(read_only=True)
    latest_status = serializers.CharField(read_only=True)

    class Meta:
        model = Repair
        fields = (
            "uuid",
            "customer",
            "code",
            "spare_part",
            "phone_lock",
            "sim_lock",
            "latest_status",
        )


class RepairSerializer(ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    spare_part = serializers.PrimaryKeyRelatedField(queryset=SparePart.objects.all())

    class Meta:
        model = Repair
        fields = (
            "uuid",
            "customer",
            "code",
            "sim_lock",
            "phone_lock",
            "spare_part",
        )


class CheckRepairStatusSerializer(ModelSerializer):
    statuses = RepairStatusSerializer(many=True)

    class Meta:
        model = Repair
        fields = ("statuses",)
