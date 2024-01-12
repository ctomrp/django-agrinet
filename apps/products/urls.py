from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('my_products/',views.myProducts,name='my_products'),
    path('create_products/', views.createProducts,name='create_products')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
