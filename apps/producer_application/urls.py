from django.urls import path
from . import  views

urlpatterns = [
    path('application_form/', views.application_form_view, name='application_form'),
    # Otras rutas si las tienes
]