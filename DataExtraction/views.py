from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from azure.cosmos import CosmosClient
from .models import SensorData
from datetime import datetime
from azure.cosmos import CosmosClient, exceptions
from django.utils.timezone import make_aware
from .serializers import SensorFisicoSerializer
from rest_framework import status
from rest_framework.response import Response


import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Acceder a las variables de entorno
credential = os.getenv('key')  
# Configura tu cliente de Azure Cosmos

cosmos_client = CosmosClient('https://cocinacosmos4.documents.azure.com:443/', credential=credential)


@api_view(['GET'])
def comprobar_conexion(request):
    try:
        # Conexión a la base de datos de Cosmos
        database_name = 'DatosCocina'
        container_name = 'sensores'
        database = cosmos_client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        # Realiza una consulta simple para comprobar la conexión
        query = "SELECT TOP 1 * FROM c"
        items = list(container.query_items(query=query, enable_cross_partition_query=True))

        if items:
            return JsonResponse({"message": "Conexión exitosa a la base de datos.", "data": items}, status=200)
        else:
            return JsonResponse({"message": "Conexión exitosa, pero no se encontraron datos."}, status=200)

    except exceptions.CosmosHttpResponseError as e:
        return JsonResponse({"message": "Error al conectarse a la base de datos.", "error": str(e)}, status=500)
    except Exception as e:
        return JsonResponse({"message": "Error inesperado.", "error": str(e)}, status=500)









@api_view(['GET'])
def guardar_datos(request):
    # Conexión a la base de datos de Cosmos
    database_name = 'DatosCocina'
    container_name = 'sensores'
    database = cosmos_client.get_database_client(database_name)
    container = database.get_container_client(container_name)

 # 1. Obtener la última fecha registrada en la base de datos
    last_sensor_data = SensorData.objects.order_by('-enqueued_time').first()

    if last_sensor_data:
        last_timestamp = last_sensor_data.enqueued_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    else:
        last_timestamp = '1900-01-01T00:00:00.000Z'

    # 2. Query ajustado para traer datos después de la última fecha registrada
    query = f"SELECT * FROM c WHERE c.enqueuedTime > '{last_timestamp}'"
    items = list(container.query_items(query=query, enable_cross_partition_query=True))

    # 3. Procesar y almacenar los nuevos datos
    for item in items:
        device_id = item['deviceId']
        template_id = item['templateId']
        timestamp = item['enqueuedTime']  # Ajusta el campo de tiempo correcto
        telemetry_data = item['telemetry']
        id_azure = item['id']  # Obtener el ID de Azure

        # Convierte el timestamp a naive datetime (sin timezone)
        naive_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')

        # Procesar cada tipo de sensor en el campo `telemetry`
        for tipo_sensor, valor in telemetry_data.items():
            sensor_data = SensorData(
                device_id=device_id,
                template_id=template_id,
                enqueued_time=naive_datetime,  # Almacena el datetime sin timezone
                tipo_sensor=tipo_sensor,
                valor=valor,
                id_azure=id_azure  # Almacena el ID de Azure
            )
            sensor_data.save()

    return JsonResponse({"message": "Datos almacenados exitosamente."}, status=200)









@api_view(['POST'])
def save_datos_fisico(request):
    serializer = SensorFisicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)