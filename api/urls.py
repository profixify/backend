from django.urls import include, path
from rest_framework import routers

from api.customer.views import CustomerViewSet
from api.repair.views import RepairViewSet
from api.settings.views import SettingsAPIView
from api.spare_part.views import SparePartViewSet

api_router = routers.DefaultRouter()
api_router.register("customers", CustomerViewSet)
api_router.register("spare-parts", SparePartViewSet)
api_router.register("repairs", RepairViewSet)

urlpatterns = [
    path("", include(api_router.urls)),
    path("settings/", SettingsAPIView.as_view(), name="settings"),
]
