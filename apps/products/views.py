
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


from .forms import CreatePrd
from .models import Product
from apps.users.views import is_userproducer
from apps.users.models import UserProducer
@login_required
@user_passes_test(is_userproducer)
def my_products(request):
    user_id = request.user.id
    products = Product.objects.filter(producer=user_id)
    return render(request, 'my_products.html', {'products': products})


@login_required
@user_passes_test(is_userproducer)
def product_detail(request, product_id):
     product = get_object_or_404(Product, pk=product_id)
   
     data = {
            'form': CreatePrd(instance=product)
     }
     
     if request.method == 'POST':
          form = CreatePrd(data=request.POST, instance=product, files=request.FILES)
          if form.is_valid():
               form.save()
               return redirect('my_products')
          
     return render(request, 'update_product.html', data) 


@login_required
@user_passes_test(is_userproducer)
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('my_products')


@login_required
@user_passes_test(is_userproducer)
def create_product(request):

    if request.method == 'GET':
            return render(request, 'create_product.html',{
                'form': CreatePrd
            }) 
    else:
        try:
            form = CreatePrd(request.POST, request.FILES)
            new_product = form.save(commit=False)
            user_id = request.user.id
            new_product.producer = UserProducer.objects.get(id=user_id)
            new_product.save()
            return redirect('my_products')
        except Exception as e:
             print(form.errors)
             print(e)
             return render(request, 'create_product.html',{
                'form': CreatePrd,
                'error': e

                })

