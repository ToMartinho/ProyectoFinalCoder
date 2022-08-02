
from django.shortcuts import render
from django.http import HttpResponse
from app_STT.models import Tipos_de_cafe, Metodo, Usuarios
from app_STT.forms import UsuarioFormulario

# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')

def tipos_de_cafe(request):

    if (request.method == 'POST'):

        cafe_tipo = Tipos_de_cafe(nombre_tipo=request.POST['cafetipo'], ingredientes=request.POST['ingredientestipo'])
        cafe_tipo.save()
        return render(request, 'inicio.html')
     
    return render (request, "TiposDeCafe.html")

def ver_tipos_cafe(self):

    lista_cafes = Tipos_de_cafe.objects.all()
    return render(self, "Listacafes.html", {"list_cafe": lista_cafes} )

def metodos(request):

    if (request.method == 'POST'):

        metodo_nombre = Metodo(nombre=request.POST['metnombre'], tipo=request.POST['mettipo'])
        metodo_nombre.save()
        return render(request, 'inicio.html')
    
    return render(request, "MetodosDeCafe.html")

def ver_lista_metodos(self):
    lista = Metodo.objects.all()
    return render(self, "lista_metodos.html", {"lista_metodos": lista})

    

def lista_usuarios(self):
    Usuario = Usuarios.objects.all()
    return render(self, "lista_usuarios.html", {"lista_usuarios": Usuario})

def crea_usuario(request):
    if request.method == 'POST':

        miFormulario = UsuarioFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = Usuarios(nombre = data['nombre'], email = data['email'])

            usuario.save()
                
            return render(request,'inicio.html')
    else:
        
        miFormulario = UsuarioFormulario()
        
        return render(request, 'usuarioFormulario.html', {'fomularioUsuario': miFormulario})
        
def buscar(request):
    if request.GET['nombre_tipo']:
        tipo_de_cafe = request.GET['nombre_tipo']

        cafe = Tipos_de_cafe.objects.filter(nombre_tipo__icontains=tipo_de_cafe)

        return render(request, 'resultadobusqueda.html',{'cafe': cafe})
    
    else:
        repuesta = "No es un tipo de cafe"

    return HttpResponse(repuesta)