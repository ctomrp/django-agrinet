from django.contrib import messages
from django.contrib.auth import login, logout, views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordResetForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from datetime import timedelta
from decouple import config
import geocoder
import json

from .forms import (
    UserClientForm,
    UserProducerForm,
    CustomAuthenticationForm,
    SalesData,
)
from .models import UserClient, UserProducer
from apps.sales.models import (
    SalesProducts,
    Sales,
    PaymentMethod,
    ReceiptType,
    ShippingMethod,
)
from apps.products.models import Product, ProductCategory
from apps.producer_application.models import ApplicationForm

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
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
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
            messages.success(request, 'Productor registrado exitosamente.')
            return redirect("admin_dashboard")
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
    products = Product.objects.filter(stock__gt=0)
    category = ProductCategory.objects.all()
    context = {'products': products,'category': category}

    return render(request, "client_dashboard.html",context)


@login_required
def custom_logout(request):
    logout(request)
    return redirect("login")


def get_address(producer_pk):
    API_KEY = config('API_KEY')
    producer = UserProducer.objects.get(pk = producer_pk)
    address = producer.address
    location = geocoder.bing(address, key=API_KEY)
    if location.ok:
        return location


@login_required
def client_product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    location = get_address(product.producer.id)
    latitude = location.lat
    longitude = location.lng
    context = {
        'product': product,
        'latitude': latitude,
        'longitude': longitude,
    }
    return render(request, 'client_product_detail.html', context)


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


@login_required
@user_passes_test(is_userclient)
def cart(request):
    items = []
    sale = []  

    if request.user.is_authenticated:
        client = request.user.userclient
        sale, created = Sales.objects.get_or_create(client=client, is_complete=False)
        items = sale.salesproducts_set.all()
    else:
        items = []
        sale = []  

    total_cart = sum([item.get_total for item in items])

    context = {'items': items, 'sales': sale, 'total_cart': total_cart}
    return render(request, 'cart.html', context)


def checkout(request):
    user_has_items_to_pay = False
    
    if request.user.is_authenticated:
        client = request.user.userclient
        sale, created = Sales.objects.get_or_create(client=client, is_complete=False)
        items = sale.salesproducts_set.all()

        arrive_date = sale.date_sale + timedelta(days=4)

        if items.exists():  
            user_has_items_to_pay = True
    else:
        items = []
        sale = []

    if not user_has_items_to_pay:
        return redirect('client_dashboard') 

    total_cart = sum([item.get_total for item in items]) 
    total_items = sum([item.quantity for item in items])

    context = {'items': items, 'sales': sale, 'total_cart': total_cart, 'total_items': total_items, 'form': SalesData, 'arrive_date':arrive_date }
    return render(request, 'checkout.html', context)


#actualizar carro
@login_required
@user_passes_test(is_userclient)
def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
 
    client = request.user.userclient
    product = Product.objects.get(id=product_id)
    sale, created = Sales.objects.get_or_create(client=client, is_complete=False)
    sale_product, created = SalesProducts.objects.get_or_create(sale=sale,product=product)
    
    if action == 'add':
        if product.stock > sale_product.quantity:
            sale_product.quantity += 1
            sale_product.save()
        else:
            return JsonResponse({'error': 'No hay suficiente stock disponible'}, status=400)
    elif action == 'remove':
        sale_product.quantity = max(0, sale_product.quantity - 1)
        sale_product.save()
    
        if sale_product.quantity == 0:
            sale_product.delete()

    return JsonResponse({'message': 'Operación exitosa'}, status=200)


@login_required
@user_passes_test(is_userclient)
def processOrder(request):
    print('Data:', request.body)
    data = json.loads(request.body)

    if request.user.is_authenticated:
        client = request.user.userclient
        sale, created = Sales.objects.get_or_create(client=client, is_complete=False)

        payment_id = data['form']['payment']
        payment_method = get_object_or_404(PaymentMethod, pk=payment_id)

        shipping_id = data['form']['shipping']
        shipping_method = get_object_or_404(ShippingMethod, pk=shipping_id)

        receipt_id = data['form']['receipt']
        receipt_type = get_object_or_404(ReceiptType, pk=receipt_id)

        sale.is_complete = True
        sale.payment = payment_method
        sale.shipping = shipping_method
        sale.receipt = receipt_type
        sale.total = data['form']['total']
        
        for sale_product in sale.salesproducts_set.all():
                product = sale_product.product
                product.stock -= sale_product.quantity
                product.save()

        sale.save()
    else:
        print('User is not logged in ')

    return JsonResponse('Payment complete ', safe=False)
