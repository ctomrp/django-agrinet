from django.urls import path
from .views import mostrar_formulario

urlpatterns = [
    path('', mostrar_formulario, name='form'),
    # Otras rutas si las tienes
]