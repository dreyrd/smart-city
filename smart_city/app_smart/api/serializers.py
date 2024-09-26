from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from app_smart.models import Sensor, Tipos_sensor
from rest_framework import serializers


class TipoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipos_sensor
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'senha': {'write_only': True}}