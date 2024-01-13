
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ApplicationForm


def application_form_view(request):
    return render(request, 'form.html')

def result_form_view(request):
    return render(request, 'resultado.html')

def guardar_formulario(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Información guardada correctamente.')
            return redirect('results')
        else:
            print('Error al guardar la información. Por favor, verifica el formulario.')
    else:
        form = ApplicationForm()

    return render(request, 'form.html', {'form': form})