from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import UserClientForm, UserProducerForm, CustomAuthenticationForm
from .models import UserClient


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

@login_required
def producer_dashboard(request):
    return render(request, "producer_dashboard.html")

@login_required
def client_dashboard(request):
    return render(request, "client_dashboard.html")

@login_required
def custom_logout(request):
    logout(request)
    return redirect("login")
