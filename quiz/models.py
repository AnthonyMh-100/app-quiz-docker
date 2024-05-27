from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(verbose_name="Nombre del Producto",max_length=20)
    imagen = models.ImageField(upload_to='productos/',verbose_name="Imagen",blank=True)
    description = models.TextField(verbose_name="Description")
    price = models.FloatField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    
    