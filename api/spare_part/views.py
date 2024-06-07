from rest_framework import viewsets

from api.spare_part.serializers import (
    SparePartBrandSerializer,
    SparePartModelSerializer,
    SparePartReadSerializer,
    SparePartSerializer,
)
from spare_part.models import Brand, Model, SparePart


class SparePartViewSet(viewsets.ModelViewSet):
    queryset = SparePart.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return SparePartSerializer
        else:
            return SparePartReadSerializer


class SparePartModelViewSet(viewsets.ModelViewSet):
    serializer_class = SparePartModelSerializer

    def get_queryset(self):
        return Model.objects.filter(brand__uuid=self.kwargs["brand_uuid"])


class SparePartBrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by("name")
    serializer_class = SparePartBrandSerializer
