from django.db.models import Case, Count, IntegerField, When
from rest_framework import generics, views
from rest_framework.response import Response

from api.dashboard.serializers import DashboardRepairListSerializer
from repair.models import Repair, RepairStatusChoices


class DashboardAPIView(generics.ListAPIView):
    queryset = Repair.objects.all()
    serializer_class = DashboardRepairListSerializer


class DashboardCountsAPIView(views.APIView):
    def get(self, request):
        repair_counts = (
            Repair.objects.annotate(
                waiting_repair=Count(
                    Case(
                        When(status=RepairStatusChoices.WAITING_REPAIR, then=1),
                        output_field=IntegerField(),
                    )
                ),
                repairing=Count(
                    Case(
                        When(status=RepairStatusChoices.REPAIRING, then=1),
                        output_field=IntegerField(),
                    )
                ),
                repaired=Count(
                    Case(
                        When(status=RepairStatusChoices.REPAIRED, then=1),
                        output_field=IntegerField(),
                    )
                ),
            )
            .values("waiting_repair", "repairing", "repaired")
            .first()
        )

        return Response(repair_counts)
