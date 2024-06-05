from rest_framework import status, views
from rest_framework.response import Response

from api.settings.serializers import SettingsSerializer
from settings.models import Settings


class SettingsAPIView(views.APIView):
    serializer_class = SettingsSerializer

    def get(self, request):
        settings = Settings.objects.first()
        serializer = SettingsSerializer(settings)
        return Response(serializer.data)

    def patch(self, request):
        settings = Settings.objects.first()
        serializer = SettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
