from django.db import models

# Create your models here.

class SensorData(models.Model):
    # Identificador del dispositivo y plantilla
    device_id = models.CharField(max_length=100)  # deviceId en los datos
    template_id = models.CharField(max_length=100)  # templateId en los datos

    # Hora en la que se hizo la medición
    enqueued_time = models.DateTimeField()  # enqueuedTime en los datos

    # Tipo de sensor y valor de la medición
    tipo_sensor = models.CharField(max_length=50)  # Identifica el tipo de sensor
    valor = models.FloatField()  # Valor del sensor (NivelDeGas, humo, PM2.5, etc.)
    id_azure = models.CharField(max_length=100, blank=True, null=True)  # Campo para el ID de Azure

    def __str__(self):
        return f"Sensor {self.tipo_sensor} (Device {self.device_id}) - Valor: {self.valor} at {self.enqueued_time}"




class SensorFisico(models.Model):
    id_registro = models.AutoField(primary_key=True)  # Genera un ID automáticamente
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha de registro
    valor_temperatura = models.FloatField()  # Valor de temperatura
    valor_humedad = models.FloatField()  # Valor de humedad

    def __str__(self):
        return f"Registro {self.id_registro} - Temp: {self.valor_temperatura}°C, Hum: {self.valor_humedad}%"