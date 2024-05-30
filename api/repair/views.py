from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from api.repair.serializers import CheckRepairStatusSerializer, RepairListSerializer, RepairSerializer
from repair.models import Repair


class RepairViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Repair.objects.select_related("customer")

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return RepairSerializer
        else:
            return RepairListSerializer

    @action(
        methods=["GET"],
        url_path="check-status/(?P<code>[^/.]+)/(?P<phone_number>[^/.]+)",
        detail=False,
        serializer_class=CheckRepairStatusSerializer,
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def check_status(self, request, code, phone_number):
        repair = get_object_or_404(
            Repair,
            code=code,
            customer__phone_number=phone_number,
        )
        serializer = CheckRepairStatusSerializer(repair)
        return Response(serializer.data)
