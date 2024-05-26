from rest_framework import serializers

from spare_part.models import SparePart


class SparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePart
        fields = (
            "uuid",
            "name",
            "price",
            "price_with_currency",
            "amount",
            "left_amount",
        )
        extra_kwargs = {
            "price": {"write_only": True},
            "left_amount": {"read_only": True},
        }
