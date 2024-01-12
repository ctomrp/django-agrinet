from django import forms
from .models import Formulario

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'