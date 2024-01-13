from django.urls import path
from .views import custom_login, producer_dashboard, client_dashboard, register_user_client, register_user_producer

urlpatterns = [
    path("", custom_login, name="login"),
    path('register/producer/', register_user_producer, name='register_user_producer'),
    path('register/client/', register_user_client, name='register_user_client'),
    path("producer/", producer_dashboard, name="producer_dashboard"),
    path("client/", client_dashboard, name="client_dashboard"),
]
