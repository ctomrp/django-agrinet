from django.urls import path
from .views import application_form_view

urlpatterns = [
    path('application_form/', application_form_view, name='application_form'),
    # Otras rutas si las tienes
]