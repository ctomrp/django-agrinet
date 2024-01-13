from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import UserProducer, UserClient


class UserProducerForm(forms.ModelForm):
    password = forms.CharField(
        label = 'Contraseña',
        widget = forms.PasswordInput(attrs={'placeholder': 'Pass "_@,.#$%&()*-+!"'})
    )
    email = forms.EmailField(
        label = 'Correo Electrónico',
        widget = forms.EmailInput(attrs={'placeholder': 'example@mail.com"'})
    )
    dni = forms.CharField(
        label = 'RUT',
        widget = forms.TextInput(attrs={'placeholder': 'Ej: 11111111-K'})
    )
    phonenumber = forms.IntegerField(
        label = 'Teléfono',
        widget = forms.NumberInput(attrs={'placeholder': 'Ej: 956800147'})
    )
    bussinessname = forms.CharField(
        label = 'Razón Social',
        widget = forms.TextInput()
    )
    class Meta:
        model = UserProducer
        fields = ["first_name", "last_name", "email", "password", "phonenumber", "bussinessname", "address", "birthdate", "dni"]
        labels = {
            'first_name': 'Primer Nombre',
            'last_name': 'Apellido Paterno',
            'address': 'Dirección',
            'birthdate': 'Fecha de Nacimiento'
        }


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
        
        
        
# login form
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Correo electrónico",
                "class": "input-text",
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Contraseña", "class": "input-text"}
        ),
    )
    

# password reset
class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')