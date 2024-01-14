from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ApplicationForm
from .models import applicationForm
from apps.users.models import ProducerType



def application_form_view(request):
    producerTypes = ProducerType.objects.all()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['rut']
            first_name = form.cleaned_data['nombre']
            last_name = form.cleaned_data['apellido']
            email = form.cleaned_data['correo']
            address = form.cleaned_data['direccion']
            phonenumber = form.cleaned_data['telefono']
            bussinessname = form.cleaned_data['razon_social']
            birthdate = form.cleaned_data['fecha_nac']
            producertype = request.POST['selectedproducertypes']
            formObj = applicationForm.objects.create(
                dni = dni, first_name = first_name, last_name = last_name,
                email = email, address = address, phonenumber = phonenumber,
                bussinessname = bussinessname, producertype = producertype, birthdate = birthdate
            )
            
            return redirect('login')

    return render(request, 'producer_application.html', {
        'form': ApplicationForm,
        'producerType': producerTypes
    })
        