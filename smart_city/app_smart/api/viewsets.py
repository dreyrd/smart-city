from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers
from rest_framework.response import Response
from rest_framework import status, viewsets
from ..models import Sensor, Tipos_sensor

class TipoSensorViewSet(viewsets.ModelViewSet):
    queryset = Tipos_sensor.objects.all()
    serializer_class = serializers.TipoSensorSerializer
    permission_classes = [permissions.IsAuthenticated]



class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class CreateUserAPIView(generics.CreateAPIView):
    query = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)