from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserClientForm

# Create your views here.


def panelControl(request):
    return render(request, 'producer_dashboard.html')

def userRegistration(request):
    if request.method == "POST":
        form = UserClientForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autenticar al usuario después de registrarse
            login(request, user)
            return redirect(
                "register_form"
            )  # Redirige a la página de inicio después del registro
    else:
        form = UserClientForm()
    return render(request, 'register_form.html', {
        'form': UserClientForm
    })
