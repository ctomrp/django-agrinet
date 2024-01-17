from django.contrib.auth import logout, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json

from .forms import UserClientForm, UserProducerForm, CustomAuthenticationForm , SalesData
from .models import UserClient
from apps.sales.models import SalesProducts, Sales, PaymentMethod, ReceiptType, ShippingMethod

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
        return super().form_invalid(form)


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


def cart(request):
    items = []
    sales = []  

    if request.user.is_authenticated:
        client = request.user.id
        sales = Sales.objects.filter(client=client)
        items = []

        for sale in sales:
            items.extend(sale.salesproducts_set.all())
            
    else:
        items = []
        sales = []  

    total_cart = sum([item.get_total for item in items])

    context = {'items': items, 'sales': sales, 'total_cart': total_cart}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        client = request.user.id
        sales = Sales.objects.filter(client=client)
        items = []

        for sale in sales:
            items.extend(sale.salesproducts_set.all())
    else:
        items = []
        sales = []  

    total_cart = sum([item.get_total for item in items])
    total_items = sum([item.quantity for item in items])

    context = {'items': items, 'sales': sales, 'total_cart': total_cart, 'total_items': total_items, 'form': SalesData }
    return render(request,'checkout.html', context)

#actualizar carro
def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
 
    client = request.user.userclient
    product = Product.objects.get(id=product_id)
    sale, created = Sales.objects.get_or_create(client=client)

    sale_product, created = SalesProducts.objects.get_or_create(sale=sale,product=product)
    
    if action == 'add':
        sale_product.quantity = (sale_product.quantity + 1) 
    elif action == 'remove':
        sale_product.quantity = (sale_product.quantity - 1) 
    
    sale_product.save()
    
    if sale_product.quantity <= 0:
        sale_product.delete()

    return JsonResponse('Item added', safe=False)

def processOrder(request):
    print('Data:', request.body)
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        client = request.user.userclient

        # Obtener o crear una instancia de Sales para el cliente
        sale, created = Sales.objects.get_or_create(client=client)

        # Convertir el valor de payment a una instancia de PaymentMethod
        payment_id = data['form']['payment']
        payment_method = get_object_or_404(PaymentMethod, pk=payment_id)

        shipping_id = data['form']['shipping']
        shipping_method = get_object_or_404(ShippingMethod, pk=shipping_id)

        receipt_id = data['form']['receipt']
        receipt_type = get_object_or_404(ReceiptType, pk=receipt_id)

        # Actualizar los campos de la instancia existente
        sale.payment = payment_method
        sale.shipping = shipping_method
        sale.receipt = receipt_type
        sale.total = data['form']['total']
        sale.save()
    else:
        print('User is not logged in ')

    return JsonResponse('Payment complete ', safe=False)