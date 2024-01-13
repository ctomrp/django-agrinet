from django.urls import path
from . import views


urlpatterns = [
    path('form/', views.application_form_view, name='application'),
    path('results/', views.result_form_view, name='results'),


    # Otras rutas si las tienes
]