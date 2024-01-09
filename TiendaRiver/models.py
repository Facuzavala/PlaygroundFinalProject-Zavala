from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="clientes_imagenes/", null=True, blank=True)
    

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Producto(models.Model):
    articulo = models.CharField(max_length=50)
    talle = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Articulo: {self.articulo} - Talle: {self.talle} - Precio: {self.precio}"

class ModoPago(models.Model):
    metodopago= models.CharField(max_length=50)
    total= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Modo de pago: {self.metodopago} - Total: {self.total}"
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"


