from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordResetView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import views as auth_views

from .forms import UserClientForm, UserProducerForm, CustomAuthenticationForm, PasswordResetRequestForm
from .models import UserClient, User
from apps.products.models import Product

from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordContextMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.edit import FormView

def is_userproducer(user):
    return hasattr(user, 'userproducer')

def is_userclient(user):
    return hasattr(user, 'userclient')

def userClientRegistration(request):
    if request.method == "POST":
        form = UserClientForm(request.POST)
        dni = form['dni'].value()
        if UserClient.objects.filter(dni=dni).exists():
            return render(request, 'client_register_form.html', {'form': form, 'user_already_exists': True})
        
        if form.is_valid():
            user = form.save()
            return redirect("client_register_form")
    else:
        form = UserClientForm()
    return render(request, 'client_register_form.html', {'form': form, 'user_already_exists': False})

def userProducerRegistration(request):
    if request.method == "POST":
        form = UserProducerForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("producer_register_form")
    return render(request, 'producer_register_form.html', {'form': UserProducerForm})


class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        user = form.get_user()

        if hasattr(user, "userproducer"):
            login(self.request, user)
            return redirect("producer_dashboard")
        elif hasattr(user, "userclient"):
            login(self.request, user)
            return redirect("client_dashboard")

        return super().form_valid(form)

class CustomPasswordResetView(PasswordContextMixin, FormView):
    email_template_name = 'registration/password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    @method_decorator(sensitive_post_parameters())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)
    
class PasswordResetRequestView(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha enviado un correo con instrucciones para restablecer la contraseña.')
        return response

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'La contraseña se ha restablecido con éxito.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'El enlace de restablecimiento de contraseña no es válido.')
        return super().form_invalid(form)

def password_reset_modal(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email)
            if users.exists():
                # Iniciar el proceso de recuperación de contraseña
                # Utiliza la vista personalizada para manejar el envío del correo electrónico
                response = CustomPasswordResetView.as_view(
                    template_name='password_reset_modal.html',
                )(request)
                messages.success(request, 'Se ha enviado un correo con instrucciones para restablecer la contraseña.')
                return response
            else:
                messages.error(request, 'El usuario con ese correo electrónico no existe.')
    else:
        form = PasswordResetForm()

    return render(request, 'password_reset_modal.html', {'form': form})

@login_required
@user_passes_test(is_userproducer)
def producer_dashboard(request):
    return render(request, "producer_dashboard.html")

@login_required
@user_passes_test(is_userclient)
def client_dashboard(request):
    products = Product.objects.all()
    return render(request, "client_dashboard.html", {'products': products})

@login_required
def custom_logout(request):
    logout(request)
    return redirect("login")


@login_required
@user_passes_test(is_userclient)
def client_product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)   
    return render(request, 'client_product_detail.html', {'product': product})

