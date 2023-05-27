from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.

def index(request):
    return render(request, "producto/index.html")

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
