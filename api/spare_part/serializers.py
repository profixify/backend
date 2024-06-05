from rest_framework import serializers

from spare_part.models import SparePart


class SparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePart
        fields = ("uuid", "name", "price", "price_with_currency", "amount", "left_amount", "temp_amount")
        extra_kwargs = {
            "left_amount": {"read_only": True},
            "temp_amount": {"read_only": True},
        }
