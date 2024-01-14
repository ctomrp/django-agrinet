from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('my_products/',views.myProducts,name='my_products'),
    path('create_products/', views.createProducts,name='create_products'),
    path('update_product/<int:product_id>', views.productDetail,name='update_product'),
    path('delete_product/<int:product_id>', views.deleteProduct,name='delete_product'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
