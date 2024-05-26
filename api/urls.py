from django.urls import include, path
from rest_framework import routers

from api.customer.views import CustomerViewSet

api_router = routers.DefaultRouter()
api_router.register("customers", CustomerViewSet)

urlpatterns = [path("", include(api_router.urls))]
