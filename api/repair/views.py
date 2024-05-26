from rest_framework import viewsets

from api.repair.serializers import RepairListSerializer, RepairSerializer
from repair.models import Repair


class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return RepairSerializer
        else:
            return RepairListSerializer
