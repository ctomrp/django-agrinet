from django import forms
from .models import UserProducer, UserClient


class UserProducerForm(forms.ModelForm):
    class Meta:
        model = UserProducer
        fields = ["first_name", "last_name", "email", "address", "birthdate", "dni"]


class UserClientForm(forms.ModelForm):
    password = forms.CharField(
        label = 'Contraseña',
        widget = forms.PasswordInput(attrs={'placeholder': 'Pass "_@,.#$%&()*-+!"'})
    )
    email = forms.EmailField(
        label = 'Correo Electrónico',
        widget = forms.EmailInput(attrs={'placeholder': 'example@mail.com"'})
    )
    dni = forms.CharField(
        label = 'RUN',
        widget = forms.TextInput(attrs={'placeholder': 'Ej: 11111111-K'})
    )
    phonenumber = forms.IntegerField(
        label = 'Teléfono',
        widget = forms.NumberInput(attrs={'placeholder': 'Ej: 956800147'})
    )
    

    class Meta:
        model = UserClient
        fields = ["first_name", "last_name", "email", "password", "phonenumber","address", "dni"]
        labels = {
            'first_name': 'Primer Nombre',
            'last_name': 'Apellido Paterno',
            'address': 'Dirección'
        }