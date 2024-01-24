from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from apps.location.models import Region, Commune
from .forms import ApplicationFormForm
from .models import ApplicationForm, ApplicationFormState
from apps.users.models import UserProducer

def create_application_form(request):
    regions = Region.objects.all()
    communes = Commune.objects.all()
    context = {
        'regions': regions,
        'communes': communes,
        'form': ApplicationFormForm
    }

    if request.method == 'POST':
        form = ApplicationFormForm(request.POST)
        if form.is_valid():
            selected_region = request.POST.get('regions')
            selected_commune = request.POST.get('communes')
            new_application = form.save(commit=False)
            new_application.address = new_application.address+', '+selected_commune+', '+selected_region
            new_application.state = ApplicationFormState.objects.get(id=10)
            new_application.save()
            return redirect('login')

    return render(request, 'producer_application.html', context)

def application_accepted(first_name, last_name, email, password):

    protocol = "http"
    domain = "127.0.0.1:8000"

    html_body = render_to_string(
        'emails/application_accepted.html', 
        {'first_name': first_name, 
        'last_name': last_name, 
        'email': email,
        'password': password,
        'domain': domain,
        'protocol': protocol 
        })

    content_text_plain = strip_tags(html_body)

    send_mail(
        'Su postulación a Productor en Agrinet ha sido aceptada',
        content_text_plain,
        'settings.EMAIL_HOST_USER',
        [email],
        html_message=html_body
    )

def application_rejected(first_name, last_name, email, reject_reason):
    protocol = "http"
    domain = "127.0.0.1:8000"

    html_body = render_to_string(
        'emails/application_rejected.html', 
        {'first_name': first_name, 
         'last_name': last_name, 
         'reject_reason': reject_reason,
         'domain': domain,
         'protocol': protocol 
         })

    content_text_plain = strip_tags(html_body)

    send_mail(
        'Su postulación a Productor en Agrinet ha sido rechazada',
        content_text_plain,
        'settings.EMAIL_HOST_USER',
        [email],
        html_message=html_body
    )

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

            first_name = producer_application_instance.first_name
            last_name = producer_application_instance.last_name
            email = producer_application_instance.email
            generated_password = generate_random_password()
            if selected_state.id == 20:
                userproducer = UserProducer(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    address = producer_application_instance.address,
                    birth_date = producer_application_instance.birth_date,
                    dni = producer_application_instance.dni,
                    business_name = producer_application_instance.bussiness_name,
                    phone_number = producer_application_instance.phone_number,
                    password = generated_password
                )
                userproducer.save()
                producer_application_instance.save()
                application_accepted(first_name=first_name, last_name=last_name, email=email, password=generated_password)
                messages.success(request, 'Productor registrado exitosamente.')
            elif selected_state.id == 30:
                application_rejected(first_name, last_name, email, feedback)

            producer_application_instance.save()
            return redirect('application_status')

    return HttpResponseBadRequest("Invalid request")


def generate_random_password():
    import secrets
    import string

    password_length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(secrets.choice(characters) for _ in range(password_length))

    return generated_password