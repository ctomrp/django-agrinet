from django.shortcuts import render, redirect
from .forms import CreatePrd
from .models import Product
# Create your views here.
def myProducts(request):
    products = Product.objects.all()
    return render(request, 'my_products.html', {'products': products})

def createProducts(request):

    if request.method == 'GET':
            return render(request, 'create_product.html',{
                'form': CreatePrd
            }) 
    else:
        try:
            form = CreatePrd(request.POST, request.FILES)
            new_product = form.save(commit=False)
            ##new_product.producer = request.user  Quitar el producer del archivo fomrs y agregar esta linea para que extraiga el producer correspondiente a la sesion iniciada
            new_product.save()
            return redirect('my_products')
        except Exception as e:
             print(form.errors)
             print(e)
             return render(request, 'create_product.html',{
                'form': CreatePrd,
                'error': e

                })
    