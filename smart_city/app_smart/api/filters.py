import django_filters
from app_smart.models import Sensor

class SensorFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(lookup_expr='icontains')
    localizacao = django_filters.CharFilter(lookup_expr='icontains')
    responsavel = django_filters.CharFilter(lookup_expr='icontains')
    status_operacional = django_filters.BooleanFilter()


    class Meta:
        model = Sensor
        fields = ['status_operacional', 'tipo', 'localizacao', 'responsavel']