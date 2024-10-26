from django.shortcuts import render

def grafana_dashboard(request):
    return render(request, 'grafana_dashboard.html')
