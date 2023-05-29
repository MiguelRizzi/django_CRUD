from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from . import models, forms
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def index(request):
    return render(request, "producto/index.html")

# Vistas basadas en clases
class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_list.html"
    context_object_name= "categorias"

class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    template_name= "producto/producto_categoria_detail.html"

class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_create.html"
    success_url = reverse_lazy("producto:producto_categoria_list")
    
class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_update.html"
    success_url = reverse_lazy("producto:producto_categoria_list")

class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_delete.html"
    success_url = reverse_lazy("producto:producto_categoria_list")



# Vistas basadas en funciones
"""
def producto_categoria_list(request):
    categorias = models.ProductoCategoria.objects.all()
    context = {"categorias": categorias}
    return render(request, "producto/producto_categoria_list.html", context)

def producto_categoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:producto_categoria_list")
    else:
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/producto_categoria_create.html", {"form": form})

def producto_categoria_update(request , id):
    categoria = models.ProductoCategoria.objects.get(id=id)
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("producto:producto_categoria_list")
    else:
        form = forms.ProductoCategoriaForm(instance=categoria)
    return render(request, "producto/producto_categoria_update.html", {"form": form})

def producto_categoria_delete(request, id):
    categoria = models.ProductoCategoria.objects.get(id=id)
    if request.method == "POST":
        categoria.delete()
        return redirect("producto:producto_categoria_list")
    return render(request, "producto/producto_categoria_delete.html", {"categoria": categoria})

def producto_categoria_detail(request: HttpRequest, pk) -> HttpResponse:
    categoria = models.ProductoCategoria.objects.get(id=pk)
    return render(request, "producto/producto_categoria_detail.html", {"object": categoria})
"""

class ProductoList(ListView):
    model = models.Producto
    context_object_name= "productos"

class ProductoDetail(DetailView):
    model = models.Producto

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    template_name = "producto/producto_create.html"
    success_url = reverse_lazy("producto:producto_list")
    
class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    template_name= "producto/producto_update.html"
    success_url = reverse_lazy("producto:producto_list")

class ProductoDelete(DeleteView):
    model = models.Producto
    template_name = "producto/producto_delete.html"
    success_url = reverse_lazy("producto:producto_list")

