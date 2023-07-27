import uuid
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    #unidad_medida = models.CharField(max_length=20)
    #tamano = models.CharField(max_length=50)
    #oferta = models.CharField(max_length=100)
    #porcentaje_oferta = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.nombre
