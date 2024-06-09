from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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
    queryset = Model.objects.all()


class SparePartBrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by("created_at")
    serializer_class = SparePartBrandSerializer

    @action(detail=True, methods=["get"])
    def models(self, request, pk):
        models = Model.objects.filter(brand__uuid=pk)
        serializer = SparePartModelSerializer(models, many=True)
        return Response(serializer.data)
