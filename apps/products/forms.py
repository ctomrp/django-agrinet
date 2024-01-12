from django import forms

from .models import Product

class CreatePrd(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'category', 'producer', 'picture']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'producer': forms.Select(attrs={'class': 'form-select'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }