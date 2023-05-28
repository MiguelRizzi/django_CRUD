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