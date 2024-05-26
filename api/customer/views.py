from rest_framework.viewsets import ModelViewSet

from api.customer.serializers import CustomerSerializer
from customer.models import Customer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
