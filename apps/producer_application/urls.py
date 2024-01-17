from django.urls import path
from . import  views

urlpatterns = [
    path('application_form/', views.application_form_view, name='application_form'),
    path('application_status/', views.list_applications, name='application_status'),
    path('application_detail/<int:application_id>/', views.application_detail, name='application_detail'),
    # Otras rutas si las tienes
]