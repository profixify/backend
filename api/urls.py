from django.urls import include, path
from rest_framework import routers

from api.customer.views import CustomerViewSet
from api.settings.views import SettingsAPIView

api_router = routers.DefaultRouter()
api_router.register("customers", CustomerViewSet)

urlpatterns = [
    path("", include(api_router.urls)),
    path("settings/", SettingsAPIView.as_view(), name="settings"),
]
