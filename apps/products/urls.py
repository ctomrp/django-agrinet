from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('create_products/', views.create_product,name='create_products'),
    path('delete_product/<int:product_id>', views.delete_product,name='delete_product'),
    path('my_products/',views.my_products,name='my_products'),
    path('update_product/<int:product_id>', views.product_detail,name='update_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
