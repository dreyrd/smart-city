from django.urls import path, include
from . import views
from app_smart.api.viewsets import CreateUserAPIView, SensorViewSet, TipoSensorViewSet, TemperaturaDataViewSet, UmidadeDataViewSet, ContadorDataViewSet, LuminosidadeDataViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from app_smart.api.filters import SensorFilterView, TemperaturaFilterView


router = DefaultRouter()
router.register(r'tipos_sensor', TipoSensorViewSet)
router.register(r'sensor', SensorViewSet)
router.register(r'temperatura', TemperaturaDataViewSet)
router.register(r'umidade', UmidadeDataViewSet)
router.register(r'contador', ContadorDataViewSet)
router.register(r'luminosidade', LuminosidadeDataViewSet)

urlpatterns = [
    path('api/enviar_csv/', views.upload_csv_view, name='enviar_csv'),
    path('api/criarusuario/', CreateUserAPIView.as_view(), name='criar_usuario'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/sensor_filter/', SensorFilterView.as_view(), name='sensor_filter'),
    path('api/temperatura_data_filter/', TemperaturaFilterView.as_view(), name='temperatura_filter'),
    
]
