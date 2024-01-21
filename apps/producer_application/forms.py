from django import forms
from .models import ApplicationForm


class ApplicationFormForm(forms.ModelForm):
    class Meta:
        model = ApplicationForm
        fields = ["first_name", "last_name", "email", "phone_number", "bussiness_name", "address", "birth_date", "dni", "state"]

    first_name = forms.CharField(
        label = 'Nombre',
        widget = forms.TextInput(attrs={'required': 'false', 'placeholder': 'John'})
    )
    last_name = forms.CharField(
        label = 'Apellido',
        widget = forms.TextInput(attrs={'required': 'false', 'placeholder': 'Doe'})
    )
    email = forms.EmailField(
        label = 'Correo Electrónico',
        widget = forms.EmailInput(attrs={'placeholder': 'johndoe@gmail.com'})
    )
    dni = forms.CharField(
        label = 'RUT',
        widget = forms.TextInput(attrs={'placeholder': '12345678-K'})
    )
    address = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(attrs={'placeholder': 'Calle Falsa 123'})
    )
    phone_number = forms.IntegerField(
        label = 'Número de Teléfono',
        widget = forms.NumberInput(attrs={'placeholder': '988776655', 'type': 'tel'})
    )
    bussiness_name = forms.CharField(
        label = 'Razón Social',
        widget = forms.TextInput(attrs={'placeholder': 'John Doe el Granjero Ltda.'})
    )
    birth_date = forms.DateField(
        label = 'Fecha de Nacimiento',
        widget = forms.DateInput(attrs={'type':'date', 'style': 'width: 190px; height: 30px;'})
    )
    state = forms.IntegerField(
        required=False,
        widget = forms.HiddenInput(attrs={'required':'False'})
    )
