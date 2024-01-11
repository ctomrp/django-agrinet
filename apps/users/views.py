from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserClientForm
# Create your views here.


def panelControl(request):
    return render(request, 'dashboard_producer.html')

def userRegistration(request):
    return render(request, 'register_form.html', {
        'form': UserClientForm
    })
