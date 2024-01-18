from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.core.mail import send_mail
from django.conf import settings

from .forms import ApplicationFormForm
from .models import ApplicationForm, ApplicationFormState

def create_application_form(request):
    if request.method == 'POST':
        form = ApplicationFormForm(request.POST)
        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.state = ApplicationFormState.objects.get(id=10)
            new_application.save()
            return redirect('login')

    return render(request, 'producer_application.html', {
        'form': ApplicationFormForm
    })

        
# @login_required  
# def list_applications(request):
#     applications = ApplicationForm.objects.all()
#     return render(request, "application_status.html", {'applications': applications})
@login_required  
def list_applications(request):
    pending_applications = ApplicationForm.objects.filter(state__id=10)

    return render(request, "application_status.html", {'pending_applications': pending_applications})


@login_required
def application_detail(request, application_id):
    application = get_object_or_404(ApplicationForm, pk=application_id)   
    application_status = ApplicationFormState.objects.all()
    context = {
        'application': application,
        'application_status': application_status
    }
    return render(request, 'application_detail.html', context)


@login_required
def update_application_form(request, application_id):
    producer_application_instance = get_object_or_404(ApplicationForm, id=application_id)

    if request.method == 'POST':
        feedback = request.POST.get('feedback', '')
        state_id = request.POST.get('state', '')
        
        if state_id:
            selected_state = ApplicationFormState.objects.get(id=state_id)
            producer_application_instance.state = selected_state


            if feedback:    
                producer_application_instance.feedback = feedback

            if selected_state.id == 20:
                send_mail(
                    'Su postulación en Agrinet ha sido aceptada',
                    'Este correo de prueba es para mostrar que su postulación fue aceptada',
                    'settings.EMAIL_HOST_USER',
                    [producer_application_instance.email]
                )
            elif selected_state.id == 30:
                send_mail(
                    'Su postulación en Agrinet ha sido rechazada',
                    'Este correo de prueba es para mostrar que su postulación fue rechazada',
                    'settings.EMAIL_HOST_USER',
                    [producer_application_instance.email]
                )

            producer_application_instance.save()
            return redirect('application_status')

    return HttpResponseBadRequest("Invalid request")