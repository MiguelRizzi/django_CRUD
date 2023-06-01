from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path("", views.index, name="index"),
    #path("producto_categoria_list/", views.producto_categoria_list, name="producto_categoria_list"),
    #path("producto_categoria_create/", views.producto_categoria_create, name="producto_categoria_create"),
    #path("producto_categoria_update/<int:id>/", views.producto_categoria_update, name="producto_categoria_update"),
    #path("producto_categoria_delete/<int:id>/", views.producto_categoria_delete, name="producto_categoria_delete"),
    path("producto_categoria_list/", views.ProductoCategoriaList.as_view(), name="producto_categoria_list"),
    path("producto_categoria_detail/<int:pk>/", views.ProductoCategoriaDetail.as_view(), name="producto_categoria_detail"),
    path("producto_categoria_create/", staff_member_required(views.ProductoCategoriaCreate.as_view()), name="producto_categoria_create"),
    path("producto_categoria_update/<int:pk>/", staff_member_required(views.ProductoCategoriaUpdate.as_view()), name="producto_categoria_update"),
    path("producto_categoria_delete/<int:pk>/", staff_member_required(views.ProductoCategoriaDelete.as_view()), name="producto_categoria_delete"),

        
    path("producto_list/", views.ProductoList.as_view(), name="producto_list"),
    path("producto_detail/<int:pk>/", views.ProductoDetail.as_view(), name="producto_detail"),
    path("producto_create/", staff_member_required(views.ProductoCreate.as_view()), name="producto_create"),
    path("producto_update/<int:pk>/", staff_member_required(views.ProductoUpdate.as_view()), name="producto_update"),
    path("producto_delete/<int:pk>/", staff_member_required(views.ProductoDelete.as_view()), name="producto_delete"),
]