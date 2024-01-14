from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserClientForm, UserProducerForm, CustomAuthenticationForm
from .models import UserClient, ProducerType, Producer_ProducerType
from apps.products.models import Product

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
            return redirect("login")
    else:
        form = UserClientForm()
    return render(request, 'client_register_form.html', {'form': form, 'user_already_exists': False})


def userProducerRegistration(request):
    producerTypes = ProducerType.objects.all()
    if request.method == "POST":
        form = UserProducerForm(request.POST)
        if form.is_valid():
            user = form.save()
            selectedProducerTypes = request.POST['selectedproducertypes']
            selectedProducerTypes = selectedProducerTypes.split(sep=',')
            for i in selectedProducerTypes:
                objProducerType = ProducerType.objects.get(id = i)
                objProducer_ProducerType = Producer_ProducerType.objects.create(
                    producerType = objProducerType,
                    producer = user
                )
                objProducer_ProducerType.save()
            return redirect("producer_register_form")
    return render(request, 'producer_register_form.html', {'form': UserProducerForm, 'producerType': producerTypes})


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

def unauthorized_access(request):
    return render(request, "unauthorized_access.html")



