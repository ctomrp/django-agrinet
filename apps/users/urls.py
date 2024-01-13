from django.urls import path

from . import views


urlpatterns = [
    path('register_client/', views.userClientRegistration, name='client_register_form'),
    path('register_producer/', views.userProducerRegistration, name='producer_register_form'),
    path("", views.CustomLoginView.as_view(), name="login"),
    path("producer/", views.producer_dashboard, name="producer_dashboard"),
    path("client/", views.client_dashboard, name="client_dashboard"),
    path('logout/', views.custom_logout, name='logout'),
]
