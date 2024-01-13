from django.urls import path

from . import views


urlpatterns = [
    path('producer_dashboard/',views.panelControl,name='producer_dashboard'),
    path('register_client/', views.userClientRegistration, name='client_register_form'),
    path('register_producer/', views.userProducerRegistration, name='producer_register_form')
]
