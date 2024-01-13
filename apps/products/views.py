
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


from .forms import CreatePrd
from .models import Product
from apps.users.views import is_userproducer

@login_required
@user_passes_test(is_userproducer)
def myProducts(request):
    products = Product.objects.all()
    return render(request, 'my_products.html', {'products': products})

@login_required
@user_passes_test(is_userproducer)
def productDetail(request, product_id):
     product = get_object_or_404(Product, pk=product_id)
   
     data = {
            'form': CreatePrd(instance=product)
     }
     
     if request.method == 'POST':
          formulario = CreatePrd(data=request.POST, instance=product, files=request.FILES)
          if formulario.is_valid():
               formulario.save()
               return redirect('my_products')
          
     return render(request, 'update_product.html', data) 


@login_required
@user_passes_test(is_userproducer)
def deleteProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('my_products')


@login_required
@user_passes_test(is_userproducer)
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
    