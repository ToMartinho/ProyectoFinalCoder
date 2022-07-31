from django.db import models


#Creacion del modelo tipos de cafe
class Tipos_de_cafe(models.Model):
    nombre_tipo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)
