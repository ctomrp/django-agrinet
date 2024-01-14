from django import forms
from .models import applicationForm

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = applicationForm
        fields = ["nombre", "apellido", "correo", "telefono", "razon_social", "direccion", "fecha_nac", "rut"]

    nombre = forms.CharField(
        label = 'Nombre',
        widget = forms.TextInput(attrs={'required': 'false'})
    )

    apellido = forms.CharField(
        label = 'Apellido'
    )
    correo = forms.EmailField(
        label = 'Correo Electrónico',
        widget = forms.EmailInput(attrs={'placeholder': 'example@mail.com"'})
    )
    rut = forms.CharField(
        label = 'RUT',
        widget = forms.TextInput(attrs={'placeholder': 'Ej: 11111111-K'})
    )
    direccion = forms.CharField(
        label='Dirección'
    )
    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget = forms.NumberInput(attrs={'placeholder': 'Ej: 956800147'})
    )
    razon_social = forms.CharField(
        label = 'Razón Social',
        widget = forms.TextInput(attrs={'placeholder': 'Agricultora Perez LTDA'})
    )
    fecha_nac = forms.DateField(
        label = 'Fecha de Nacimiento',
        widget = forms.DateInput(attrs={'type':'date', 'style': 'width: 190px; height: 30px;'})
    )
