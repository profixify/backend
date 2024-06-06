from rest_framework import serializers

from api.spare_part.serializers import SparePartSerializer
from customer.models import Customer
from repair.models import Repair


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "uuid",
            "first_name",
            "last_name",
            "full_name",
            "phone_number",
        )


class CustomerRepairSerializer(serializers.ModelSerializer):
    spare_part = SparePartSerializer(read_only=True)
    latest_status = serializers.CharField()

    class Meta:
        model = Repair
        fields = (
            "code",
            "sim_lock",
            "phone_lock",
            "spare_part",
            "latest_status",
        )
