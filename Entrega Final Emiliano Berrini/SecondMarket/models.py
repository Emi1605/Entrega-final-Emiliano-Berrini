from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    Nombre_Producto = models.CharField(max_length=30)
    Precio_Producto = models.IntegerField()
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=120)
    DueñoPost = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="DueñoPost")
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)
    Creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.Nombre_Producto} - {self.Precio_Producto} - {self.cantidad} - {self.Creado_el}"


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")    
    imagen = models.ImageField(upload_to="profiles", null=True, blank=True)

class Mensaje(models.Model):
      mensaje = models.TextField(max_length=1000)
      mail = models.EmailField()
      destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name= "destinatario")