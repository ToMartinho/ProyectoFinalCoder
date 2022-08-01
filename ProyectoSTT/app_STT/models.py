import email
from django.db import models


#Creacion del modelo tipos de cafe
class Tipos_de_cafe(models.Model):
    nombre_tipo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)

class Metodo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    