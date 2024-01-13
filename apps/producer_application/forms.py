from django import forms
from .models import formulario

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = formulario
        fields = ['rut','nombre','apellido','edad','correo','telefono','razon_social','tipo_productor','fecha_nac']