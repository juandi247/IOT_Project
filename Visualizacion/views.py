from django.shortcuts import render
import requests

def grafana_dashboard(request):
    grafana_url = "http://localhost:3000/api/dashboards/uid/your_dashboard_id"
    headers = {
        "Authorization": "Bearer your_api_key"
    }

    response = requests.get(grafana_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Pasa los datos obtenidos a la plantilla de Django
        return render(request, 'grafana_dashboard.html', {'dashboard_data': data})
    else:
        return render(request, 'grafana_dashboard.html', {'error': 'Error al obtener datos de Grafana'})
