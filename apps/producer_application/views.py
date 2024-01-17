from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404


from .forms import ApplicationFormForm
from .models import ApplicationForm

def application_form_view(request):
    if request.method == 'POST':
        form = ApplicationFormForm(request.POST)
        if form.is_valid():
            """
            dni = form.cleaned_data['rut']
            first_name = form.cleaned_data['nombre']
            last_name = form.cleaned_data['apellido']
            email = form.cleaned_data['correo']
            address = form.cleaned_data['direccion']
            phone_number = form.cleaned_data['telefono']
            bussiness_name = form.cleaned_data['razon_social']
            birth_date = form.cleaned_data['fecha_nac']
            form_obj = ApplicationForm.objects.create(
                dni = dni, first_name = first_name, last_name = last_name,
                email = email, address = address, phone_number = phone_number,
                bussiness_name = bussiness_name, birth_date = birth_date
            )
            """
            form.save()
            return redirect('login')

    return render(request, 'producer_application.html', {
        'form': ApplicationFormForm
    })
    
   
        
@login_required  
def list_applications(request):
    applications = ApplicationForm.objects.all()
    return render(request, "application_status.html", {'applications': applications})


@login_required
def application_detail(request, application_id):
    application = get_object_or_404(ApplicationForm, pk=application_id)   
    return render(request, 'application_detail.html', {'application': application})