from django.db.models import Case, Count, IntegerField, Sum, Value, When
from django.db.models.functions import Coalesce
from rest_framework import generics, views
from rest_framework.response import Response

from api.dashboard.serializers import DashboardRepairListSerializer
from repair.models import Repair, RepairStatusChoices


class DashboardAPIView(generics.ListAPIView):
    queryset = Repair.objects.all()
    serializer_class = DashboardRepairListSerializer


class DashboardCountsAPIView(views.APIView):
    def get(self, request):
        aggretations = {
            choice.lower(): Count(
                Case(
                    When(statuses__status=choice, then=1),
                    output_field=IntegerField(),
                )
            )
            for choice in dict(RepairStatusChoices.choices)
        }
        repair_counts = Repair.objects.aggregate(**aggretations)
        return Response(repair_counts)
