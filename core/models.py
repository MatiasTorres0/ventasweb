import uuid
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo_barras = models.CharField(max_length=200, null=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField(null=True)
    stock = models.IntegerField( null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    unidad_medida = models.CharField(max_length=20, null=True)
    tamano = models.CharField(max_length=50, null=True)
    oferta = models.CharField(max_length=100, null=True)
    descuento = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.nombre
