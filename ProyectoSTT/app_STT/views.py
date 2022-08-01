from django.http import HttpResponse
from django.shortcuts import render

from ProyectoSTT.app_STT.models import Metodo

# Create your views here.
def metodos(self, nombre, tipo):
    metodos = Metodo(nombre = nombre, tipo = tipo)
    metodos.save()

    return HttpResponse(f'Los siguientes son metodos de extración de café')

def lista_metodos(self):
    lista = Metodo.objects.all()
    return render(self, "lista_metodos.html", {"lista_metodos": lista})