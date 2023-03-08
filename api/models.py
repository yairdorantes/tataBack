from django.db import models

class Ventas(models.Model):
    cliente = models.CharField(max_length=100)
    fecha = models.DateField()
    hora  = models.TimeField()
    total = models.FloatField()
    
    def __str__(self) -> str:
        return self.cliente
class Products(models.Model):
    name = models.CharField(max_length=200)
    image=  models.TextField()
    price = models.FloatField()
     
    def __str__(self) -> str:
        return self.name
class Clients(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100,default="")
    
    def __str__(self) -> str:
        return self.name
    
class Providers(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    producto = models.CharField(max_length=200)
    image = models.TextField()
    def __str__(self) -> str:
        return self.name