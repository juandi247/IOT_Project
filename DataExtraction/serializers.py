# serializers.py

from rest_framework import serializers
from .models import SensorFisico

class SensorFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorFisico
        fields = ['fecha_registro','valor_temperatura', 'valor_humedad']  # Excluye el id_registro y fecha_registro
