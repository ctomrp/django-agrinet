from django import forms
from .models import UserProducer, UserClient


class UserProducerForm(forms.ModelForm):
    class Meta:
        model = UserProducer
        fields = ["first_name", "last_name", "email", "address", "birthdate", "dni"]


class UserClientForm(forms.ModelForm):
    class Meta:
        model = UserClient
        fields = ["first_name", "last_name", "email", "password", "phonenumber","address", "dni"]
        labels = {
            'first_name': 'Primer Nombre',
            'last_name': 'Apellido Paterno',
            'email': 'Correo Electrónico',
            'password': 'Contraseña',
            'phonenumber': "Teléfono",
            'address': 'Dirección',
            'dni': 'RUN'
        }
