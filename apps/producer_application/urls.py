from django.urls import path
from .views import application_form_view

urlpatterns = [
    path('', application_form_view, name='application'),
    # Otras rutas si las tienes
]