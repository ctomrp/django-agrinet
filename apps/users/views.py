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

def myProducts(request):
    return render(request, 'my_products.html')
