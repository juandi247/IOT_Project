from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.grafana_dashboard, name='grafana_dashboard'),
    path('index/', views.index, name='index'),
]
