from django.db.models import OuterRef, Subquery
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.customer.serializers import CustomerRepairSerializer, CustomerSerializer
from customer.models import Customer
from repair.models import Repair, RepairStatus


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=["get"], url_path="repairs")
    def repairs(self, request, pk=None):
        repairs = Repair.objects.filter(customer__uuid=pk).annotate(
            latest_status=Subquery(
                RepairStatus.objects.filter(repair__uuid=OuterRef("uuid")).order_by("-created_at").values("status")[:1]
            )
        )
        serializer = CustomerRepairSerializer(repairs, many=True)
        return Response(serializer.data)
