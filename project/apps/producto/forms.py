from django import forms
from django.forms import ModelForm
from . import models



class ProductoCategoriaForm(ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'precio', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }