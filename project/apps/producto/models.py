from django.db import models

# Create your models here.
class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria de producto'
        verbose_name_plural = "Categorias de productos"

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.FloatField()
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre