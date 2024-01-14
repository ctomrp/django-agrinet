from django import forms
from .models import formulario

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = formulario
        fields = ['rut','nombre','apellido','correo','telefono','razon_social','tipo_productor','fecha_nac']



    nombre = forms.CharField(
        label = 'Nombre',
        widget = forms.PasswordInput(attrs={'placeholder': 'Pass "_@,.#$%&()*-+!"'})
    )

    apellido = forms.CharField(
        label = 'Apellido',
        widget = forms.PasswordInput(attrs={'placeholder': 'Pass "_@,.#$%&()*-+!"'})
    )
    correo = forms.EmailField(
        label = 'Correo Electrónico',
        widget = forms.EmailInput(attrs={'placeholder': 'example@mail.com"'})
    )
    rut = forms.CharField(
        label = 'RUT',
        widget = forms.TextInput(attrs={'placeholder': 'Ej: 11111111-K'})
    )
    telefono = forms.IntegerField(
        label = 'Teléfono',
        widget = forms.NumberInput(attrs={'placeholder': 'Ej: 956800147'})
    )
    razon_social = forms.CharField(
        label = 'Razón Social',
        widget = forms.TextInput(attrs={'placeholder': 'AgricultoraPerez.LTDA'})
    )
    fecha_nac = forms.DateField(
        label = 'Fecha de Nacimiento',
        widget = forms.DateInput(attrs={'type':'date', 'style': 'width: 190px; height: 30px;'})
    )
  
   
