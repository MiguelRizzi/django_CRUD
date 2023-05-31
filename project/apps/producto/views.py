from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from . import models, forms
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



# Vistas basadas en funciones
@login_required
def index(request):
    return render(request, "producto/index.html")

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


# Vistas basadas en clases

#class IndexView(TemplateView):
#   template_name = "producto/index.html"

class ProductoCategoriaList(LoginRequiredMixin, ListView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_list.html"
    context_object_name= "categorias"
    def get_queryset(self):
        # Si la búsqueda tiene algún texto introducido, devuelve todos los productos que contengan dicho texto
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre__icontains=query)
        # Si no, devuelve todos los productos
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list
        

class ProductoCategoriaDetail(LoginRequiredMixin, DetailView):
    model = models.ProductoCategoria
    template_name= "producto/producto_categoria_detail.html"

class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_form.html"
    success_url = reverse_lazy("producto:producto_categoria_list")
    
class ProductoCategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_form.html"
    success_url = reverse_lazy("producto:producto_categoria_list")

class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_confirm_delete.html"
    success_url = reverse_lazy("producto:producto_categoria_list")


class ProductoList(LoginRequiredMixin, ListView):
    model = models.Producto
    context_object_name= "productos"

class ProductoDetail(LoginRequiredMixin, DetailView):
    model = models.Producto

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")
    
class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")

