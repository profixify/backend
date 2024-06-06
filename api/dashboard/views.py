from django.db.models import Case, Count, IntegerField, OuterRef, Subquery, When
from rest_framework import generics, views
from rest_framework.response import Response

from api.dashboard.serializers import DashboardRepairListSerializer
from repair.models import Repair, RepairStatus, RepairStatusChoices


class DashboardAPIView(generics.ListAPIView):
    queryset = Repair.objects.all()
    serializer_class = DashboardRepairListSerializer


class DashboardCountsAPIView(views.APIView):
    def get(self, request):
        latest_status_subquery = (
            RepairStatus.objects.filter(repair=OuterRef("pk")).order_by("-created_at").values("status")[:1]
        )

        repairs = Repair.objects.annotate(latest_status=Subquery(latest_status_subquery))

        aggretations = {
            choice.lower(): Count(
                Case(
                    When(latest_status=choice, then=1),
                    output_field=IntegerField(),
                )
            )
            for choice in dict(RepairStatusChoices.choices)
        }
        repair_counts = repairs.aggregate(**aggretations)
        return Response(repair_counts)
