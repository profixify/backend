from django.db.models import OuterRef, Subquery
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from api.repair.serializers import (
    CheckRepairStatusSerializer,
    RepairReadSerializer,
    RepairSerializer,
    RepairStatusSerializer,
)
from repair.models import Repair, RepairStatus


class RepairViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Repair.objects.select_related("customer").annotate(
            latest_status=Subquery(
                RepairStatus.objects.filter(repair__uuid=OuterRef("uuid")).order_by("-created_at").values("status")[:1]
            )
        )

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return RepairSerializer
        else:
            return RepairReadSerializer

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
        return Response(serializer.data["statuses"])


class RepairStatusViewSet(viewsets.ModelViewSet):
    serializer_class = RepairStatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return RepairStatus.objects.filter(repair__uuid=self.kwargs["repair_uuid"])

    def perform_create(self, serializer):
        repair = Repair.objects.get(uuid=self.kwargs["repair_uuid"])
        serializer.save(repair=repair)
