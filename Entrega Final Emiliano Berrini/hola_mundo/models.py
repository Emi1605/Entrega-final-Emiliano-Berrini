from django.db import models

class producto(models.Model):

    nombre_Producto =  models.CharField(max_length=100)
    precio_unidad = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + "-" + self.nombre_Producto + "-" + str(self.precio_unidad) + "-" + self.descripcion

class venta(models.Model):
    
    nombre_comprador = models.CharField(max_length=100)
    apellido_comprador = models.CharField(max_length=100)
    numero_venta = models.IntegerField()
    compra = models.CharField(max_length=100)

    def __str__(self):
         return str(self.id) + "-" + self.nombre_comprador + "-" + self.apellido_comprador + "-" + str(self.numero_venta) + "-" + self.compra
        
class persona(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.id} {self.nombre} - {self.apellido} "
