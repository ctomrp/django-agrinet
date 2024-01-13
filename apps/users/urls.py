from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register_client/', views.userClientRegistration, name='client_register_form'),
    path('register_producer/', views.userProducerRegistration, name='producer_register_form'),
    path("", views.CustomLoginView.as_view(), name="login"),
    path("producer/", views.producer_dashboard, name="producer_dashboard"),
    path("client/", views.client_dashboard, name="client_dashboard"),
    path('logout/', views.custom_logout, name='logout'),
    path('client/<int:product_id>', views.client_product_detail,name='client_product_detail'),
    path("unauthorized_access", views.unauthorized_access, name="unauthorized_access"),
]
