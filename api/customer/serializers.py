from rest_framework import serializers

from api.spare_part.serializers import SparePartSerializer
from customer.models import Customer
from repair.models import Repair


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "uuid",
            "name",
            "surname",
            "full_name",
            "identity_number",
            "phone_number",
        )
        extra_kwargs = {"name": {"write_only": True}, "surname": {"write_only": True}}


class CustomerRepairSerializer(serializers.ModelSerializer):
    spare_part = SparePartSerializer(read_only=True)

    class Meta:
        model = Repair
        fields = (
            "code",
            "sim_lock",
            "phone_lock",
            "spare_part",
            "status",
        )
