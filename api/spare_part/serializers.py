from rest_framework import serializers

from spare_part.models import Brand, Model, SparePart


class SparePartBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("uuid", "name")


class SparePartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ("uuid", "name", "brand")


class SparePartModelReadSerializer(serializers.ModelSerializer):
    brand = SparePartBrandSerializer(read_only=True)

    class Meta:
        model = Model
        fields = ("uuid", "name", "brand")


class SparePartSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    model = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all())

    class Meta:
        model = SparePart
        fields = (
            "uuid",
            "name",
            "brand",
            "model",
            "price",
            "price_with_currency",
            "amount",
            "left_amount",
            "temp_amount",
        )
        extra_kwargs = {
            "left_amount": {"read_only": True},
            "temp_amount": {"read_only": True},
        }


class SparePartReadSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return obj.brand.name

    def get_model(self, obj):
        return obj.model.name

    class Meta:
        model = SparePart
        fields = (
            "uuid",
            "name",
            "brand",
            "model",
            "price",
            "price_with_currency",
            "amount",
            "left_amount",
            "temp_amount",
        )
        extra_kwargs = {
            "left_amount": {"read_only": True},
            "temp_amount": {"read_only": True},
        }
