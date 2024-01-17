from django.contrib.auth import logout, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserClientForm, UserProducerForm, CustomAuthenticationForm
from .models import UserClient

from .models import UserClient
from apps.products.models import Product
from django.db.models import Q


def is_userproducer(user):
    return hasattr(user, 'userproducer')


def is_userclient(user):
    return hasattr(user, 'userclient')



def user_client_registration(request):
    if request.method == "POST":
        form = UserClientForm(request.POST)
        dni = form['dni'].value()
        if UserClient.objects.filter(dni=dni).exists():
            return render(request, 'client_register_form.html', {'form': form, 'user_already_exists': True})
        
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserClientForm()
    return render(request, 'client_register_form.html', {'form': form, 'user_already_exists': False})

@login_required
def user_producer_registration(request):
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
        elif user.is_superuser:
            login(self.request, user)
            return redirect("admin_dashboard")
        return super().form_invalid(form)
    
@login_required
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


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
# @user_passes_test(is_userclient)
def client_product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)   
    return render(request, 'client_product_detail.html', {'product': product})


def unauthorized_access(request):
    return render(request, "unauthorized_access.html")


# formulario modal
def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                return render(request, "password_reset_done.html", {'email': email})
            except User.DoesNotExist:
                pass

        form = PasswordResetForm(request.POST)
        if form.is_valid():
            return auth_views.password_reset()

    else:
        form = PasswordResetForm()

    return render(request, "password_reset.html", {'form': form})


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_products.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        print(query)
        if query:
            print(query)
            queryset = Product.objects.filter(
            Q(description__icontains=query)
            ) 
            return queryset
        else:
            return Product.objects.none()
