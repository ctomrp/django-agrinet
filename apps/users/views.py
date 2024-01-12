
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render

from django.http import HttpResponseForbidden

from .models import UserProducer
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
    ###if request.user.is_authenticated and isinstance(request.user, UserProducer):
     ##   return render(request, "producer_dashboard.html")
   ## else:
     ##   return HttpResponseForbidden("Acceso denegado")
    return render(request, "producer_dashboard.html")

def client_dashboard(request):
    return render(request, "client_dashboard.html")

