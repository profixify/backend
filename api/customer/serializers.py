from rest_framework import serializers

from customer.models import Customer


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
