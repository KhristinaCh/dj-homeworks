from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.select_related()
    serializer_class = MeasurementSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.select_related()
    serializer_class = SensorDetailSerializer
