from django import forms
from django.forms import ModelForm
from . import models

class ProductoCategoriaForm(ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = '__all__'
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_actualizacion': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
