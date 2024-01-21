from django import forms
from .models import ApplicationForm


class ApplicationFormForm(forms.ModelForm):
    class Meta:
        model = ApplicationForm
        fields = ["first_name", "last_name", "email", "phone_number", "bussiness_name", "address", "birth_date", "dni", "state"]

    first_name = forms.CharField(
        label = 'Nombre',
        widget = forms.TextInput(attrs={'required': 'false'})
    )
    last_name = forms.CharField(
        label = 'Apellido'
    )
    email = forms.EmailField(
        label = 'Correo Electrónico',
        widget = forms.EmailInput(attrs={'placeholder': 'example@mail.com"'})
    )
    dni = forms.CharField(
        label = 'RUT',
        widget = forms.TextInput(attrs={'placeholder': 'Ej: 11111111-K'})
    )
    address = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(attrs={'placeholder': 'Ej: Nombre calle 1234'})
    )
    phone_number = forms.IntegerField(
        label = 'Número de Teléfono',
        widget = forms.NumberInput(attrs={'placeholder': 'Ej: 956800147', 'type': 'tel'})
    )
    bussiness_name = forms.CharField(
        label = 'Razón Social',
        widget = forms.TextInput(attrs={'placeholder': 'Agricultora Perez LTDA'})
    )
    birth_date = forms.DateField(
        label = 'Fecha de Nacimiento',
        widget = forms.DateInput(attrs={'type':'date', 'style': 'width: 190px; height: 30px;'})
    )
    state = forms.IntegerField(
        required=False,
        widget = forms.HiddenInput(attrs={'required':'False'})
    )
