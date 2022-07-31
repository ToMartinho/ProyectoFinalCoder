from django.shortcuts import render
from app_STT.models import Tipos_de_cafe

# Create your views here.

def inicio(request):

    return render(request, 'index.html')

def tipos_de_cafe(request):

    if (request.method == 'POST'):

        cafe_tipo = Tipos_de_cafe(nombre_tipo=request.POST['cafetipo'], ingredientes=request.POST['ingredientestipo'])
        cafe_tipo.save()
        return render(request, 'index.html')
     
    return render (request, "TiposDeCafe.html")

def ver_tipos_cafe(self):

    lista_cafes = Tipos_de_cafe.objects.all()
    return render(self, "Listacafes.html", {"list_cafe": lista_cafes} )
    
