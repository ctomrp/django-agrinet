from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import UserProducer, UserClient


class UserProducerForm(forms.ModelForm):
    class Meta:
        model = UserProducer
        fields = ["first_name", "last_name", "email", "address", "birthdate", "dni" , "password"]


class UserClientForm(forms.ModelForm):
    class Meta:
        model = UserClient
        fields = ["first_name", "last_name", "email", "address", "dni","password"]
        

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

