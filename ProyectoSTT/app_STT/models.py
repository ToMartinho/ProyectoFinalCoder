from distutils.command.upload import upload
import email
from enum import unique
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


#Creacion del modelo tipos de cafe
class Tipos_de_cafe(models.Model):
    nombre_tipo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='default.jpg', upload_to='cafes', null=True,blank = True)
    fecha = models.DateTimeField(auto_now_add=True,auto_now=False)
   

class Metodo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='default.jpg', upload_to='avatares', null=True,blank = True, unique=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

#class Bio(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #bio = models.TextField(null=True, blank=True)
    #link = models.URLField(max_length=200, null=True, blank=True)