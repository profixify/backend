from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.customer.views import CustomerViewSet
from api.dashboard.views import DashboardAPIView, DashboardCountsAPIView
from api.repair.views import RepairViewSet
from api.settings.views import SettingsAPIView
from api.spare_part.views import SparePartViewSet

api_router = routers.DefaultRouter()
api_router.register("customers", CustomerViewSet)
api_router.register("spare-parts", SparePartViewSet)
api_router.register("repairs", RepairViewSet, basename="repair")

urlpatterns = [
    path("", include(api_router.urls)),
    path("settings/", SettingsAPIView.as_view(), name="settings"),
    path("dashboard/", DashboardAPIView.as_view(), name="dashboard"),
    path("dashboard-counts/", DashboardCountsAPIView.as_view(), name="dashboard-counts"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
