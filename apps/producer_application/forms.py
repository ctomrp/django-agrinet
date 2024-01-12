from django import forms
from .models import formulario

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = formulario
        fields = '__all__'