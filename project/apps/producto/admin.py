from django.contrib import admin

from . import models
# Register your models here.


admin.site.site_tittle = "Productos"
admin.site.site_header = "My app Django - Productos"

#admin.site.register(models.ProductoCategoria)
@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "categoria")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
  