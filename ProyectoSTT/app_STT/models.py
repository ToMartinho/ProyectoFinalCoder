from distutils.command.upload import upload
import email
from django.db import models
from django.contrib.auth.models import User


#Creacion del modelo tipos de cafe
class Tipos_de_cafe(models.Model):
    nombre_tipo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)
   

class Metodo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    
class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True,blank = True)