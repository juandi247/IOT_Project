from django.urls import path
from .views import *

urlpatterns=[
    path('extract_data_azure',guardar_datos),
    path('save_datos_fisico',save_datos_fisico),
]