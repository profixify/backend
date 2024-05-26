from rest_framework import viewsets

from api.spare_part.serializers import SparePartSerializer
from spare_part.models import SparePart


class SparePartViewSet(viewsets.ModelViewSet):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer
