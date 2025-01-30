from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=500)
    costo = models.FloatField()

    def __str__(self):
        return self.nombre