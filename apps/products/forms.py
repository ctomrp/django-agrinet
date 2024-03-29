from django import forms

from .models import Product


class CreatePrd(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'category', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre',
            'price': 'Precio x Kilo',
            'stock': 'Cantidad en inventario',
            'description': 'Descripción',
            'category': 'Categoría',
            'picture': 'Imagen',
        }
