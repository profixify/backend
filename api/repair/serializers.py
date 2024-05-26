from rest_framework import serializers

from api.customer.serializers import CustomerSerializer
from api.spare_part.serializers import SparePartSerializer
from customer.models import Customer
from repair.models import Repair
from spare_part.models import SparePart


class RepairListSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    spare_part = SparePartSerializer(read_only=True)

    class Meta:
        model = Repair
        fields = (
            "uuid",
            "customer",
            "code",
            "spare_part",
            "phone_lock",
            "sim_lock",
            "status",
        )


class RepairSerializer(serializers.ModelSerializer):
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
            "status",
        )
