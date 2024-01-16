from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationFormForm
from .forms import ApplicationForm  

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
        

def edit_application_form(request, form_id):
    existing_form = get_object_or_404(ApplicationForm, id=form_id)

    if request.method == 'POST':
        form = ApplicationFormForm(request.POST, instance=existing_form)
        if form.is_valid():
            form.save()
            return redirect('login')

    form_list = ApplicationForm.objects.all()

    return render(request, 'producer_application.html', {
        'form': form,
        'form_list': form_list
    })

def delete_application_form(request, form_id):
    existing_form = get_object_or_404(ApplicationForm, id=form_id)

    if request.method == 'POST':
        existing_form.delete()
        return redirect('login')

    form_list = ApplicationForm.objects.all()

    return render(request, 'producer_application.html', {
        'form': ApplicationFormForm(),
        'form_list': form_list
    })