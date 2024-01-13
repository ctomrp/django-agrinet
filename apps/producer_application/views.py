
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ApplicationForm



def result_form_view(request):
    return render(request, 'producer_application.html')


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

    if request.method == 'GET':
            return render(request, 'producer_application.html',{
                'form': ApplicationForm
            }) 

    else:
        try:
            form = ApplicationForm(request.POST)
            new_application = form.save(commit=False)
            new_application.save()
            return redirect('/')
        except Exception as e:
             return render(request, 'producer_application.html',{
                'form': ApplicationForm,
                'error': e

                })
    
