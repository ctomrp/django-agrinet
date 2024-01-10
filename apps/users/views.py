from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def panelControl(request):
    return render(request, 'dashboard_producer.html')