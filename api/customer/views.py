from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.customer.serializers import CustomerRepairSerializer, CustomerSerializer
from customer.models import Customer
from repair.models import Repair


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=["get"], url_path="repairs")
    def repairs(self, request, pk=None):
        repairs = Repair.objects.filter(customer__uuid=pk)
        serializer = CustomerRepairSerializer(repairs, many=True)
        return Response(serializer.data)
