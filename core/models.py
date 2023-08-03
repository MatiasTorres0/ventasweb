import uuid
from django.db import models
from django.contrib.auth.models import User



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
    imagen = models.FileField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen o Video")
    unidad_medida = models.CharField(max_length=20, null=True)
    tamano = models.CharField(max_length=50, null=True)
    oferta = models.CharField(max_length=100, null=True)
    descuento = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario que generó la boleta
    nro_boleta = models.CharField(max_length=20, unique=True)  # Número de la boleta
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    archivo_pdf = models.FileField(upload_to='boletas/')

    def __str__(self):
        return f"Boleta #{self.nro_boleta} - Usuario: {self.usuario.username} - Total: ${self.total_a_pagar}"
    

    
class Conversacion(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Conversación {self.id}'

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Mensaje de {self.remitente} en Conversación {self.conversacion.id}'