from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        user = form.get_user()

        if hasattr(user, "userproducer"):
            return redirect("producer_dashboard")
        elif hasattr(user, "userclient"):
            return redirect("client_dashboard")

        return super().form_valid(form)


def producer_dashboard(request):
    return render(request, "producer_dashboard.html")


def client_dashboard(request):
    return render(request, "client_dashboard.html")

from django.shortcuts import render, redirect
from .forms import UserProducerForm, UserClientForm
from django.contrib.auth import authenticate, login


def register_user_producer(request):
    if request.method == "POST":
        form = UserProducerForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autenticar al usuario después de registrarse
            login(request, user)
            return redirect(
                "register_user_producer"
            )  # Redirige a la página de inicio después del registro
    else:
        form = UserProducerForm()

    return render(request, "register_user_producer.html", {"form": form})


def register_user_client(request):
    if request.method == "POST":
        form = UserClientForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autenticar al usuario después de registrarse
            login(request, user)
            return redirect(
                "register_user_client"
            )  # Redirige a la página de inicio después del registro
    else:
        form = UserClientForm()

    return render(request, "register_user_client.html", {"form": form})