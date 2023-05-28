from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("producto_categoria_list/", views.producto_categoria_list, name="producto_categoria_list"),
    #path("producto_categoria_create/", views.producto_categoria_create, name="producto_categoria_create"),
    #path("producto_categoria_update/<int:id>/", views.producto_categoria_update, name="producto_categoria_update"),
    #path("producto_categoria_delete/<int:id>/", views.producto_categoria_delete, name="producto_categoria_delete"),
    path("producto_categoria_list/", views.ProductoCategoriaList.as_view(), name="producto_categoria_list"),
    path("producto_categoria_create/", views.ProductoCategoriaCreate.as_view(), name="producto_categoria_create"),
    path("producto_categoria_update/<int:pk>/", views.ProductoCategoriaUpdate.as_view(), name="producto_categoria_update"),
    path("producto_categoria_delete/<int:pk>/", views.ProductoCategoriaDelete.as_view(), name="producto_categoria_delete"),
]