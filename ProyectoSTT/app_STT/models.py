from django.db import models

# Create your models here.
class Metodo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)