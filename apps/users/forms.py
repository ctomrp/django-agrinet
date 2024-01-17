from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.sales.models import Sales
from .models import UserProducer, UserClient

class SalesData(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['shipping','payment','receipt']
        widgets = {
            'shipping': forms.Select(attrs={'class': 'form-select'}),
            'payment': forms.Select(attrs={'class': 'form-select'}),
            'receipt': forms.Select(attrs={'class': 'form-select'}),
        }


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
    phone_number = forms.IntegerField(
        label = 'Teléfono',
        widget = forms.NumberInput(attrs={'placeholder': 'Ej: 956800147', 'type': 'tel'})
    )
    bussiness_name = forms.CharField(
        label = 'Razón Social',
        widget = forms.TextInput()
    )
    birth_date = forms.DateField(
        label = 'Fecha de Nacimiento',
        widget = forms.DateInput(attrs={'type':'date', 'style': 'width: 190px; height: 30px;'})
    )

    class Meta:
        model = UserProducer
        fields = ["first_name", "last_name", "email", "password", "phone_number", "bussiness_name", "address", "birth_date", "dni"]
        labels = {
            'first_name': 'Primer Nombre',
            'last_name': 'Apellido Paterno',
            'address': 'Dirección',
            'birth_date': 'Fecha de Nacimiento'
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
    phone_number = forms.IntegerField(
        label = 'Teléfono',
        widget = forms.NumberInput(attrs={'placeholder': 'Ej: 956800147', 'type': 'tel'})
    )
    class Meta:
        model = UserClient
        fields = ["first_name", "last_name", "email", "password", "phone_number","address", "dni"]
        labels = {
            'first_name': 'Primer Nombre',
            'last_name': 'Apellido Paterno',
            'address': 'Dirección'
        }


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


