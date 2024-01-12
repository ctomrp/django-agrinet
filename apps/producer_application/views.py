from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import formulario
from .forms import ApplicationForm


def application_form_view(request):
    return render(request, 'form.html')


class formularioView(HttpRequest):

    def index (request):
        formulario = formulario()
        return render(request,"form.html", {"form": formulario})
    
    def guardar_formulario(request):
        formulario = formulario()
        if formulario.is_valid():
            formulario.save()
            formulario = formulario()

            return render(request, "form.html", {"form": formulario, "mensaje": 'Ok'})