
from django.shortcuts import render
from django.http import HttpResponse
from app_STT.models import Tipos_de_cafe, Metodo
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import DetailView
from app_STT.forms import RegistroUsuario
from django.views.generic import DeleteView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en CLASES
from django.contrib.auth.decorators import login_required #para vistas basadas en FUNCIONES


# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')

@login_required
def tipos_de_cafe(request):

    if (request.method == 'POST'):

        cafe_tipo = Tipos_de_cafe(nombre_tipo=request.POST['cafetipo'], ingredientes=request.POST['ingredientestipo'])
        cafe_tipo.save()
        return render(request, 'inicio.html')
     
    return render (request, "TiposDeCafe.html")


def ver_tipos_cafe(self):

    lista_cafes = Tipos_de_cafe.objects.all()
    return render(self, "Listacafes.html", {"lista_cafes": lista_cafes} )

@login_required
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
    Usuario = User.objects.all()
    return render(self, "lista_usuarios.html", {"lista_usuarios": Usuario})

        
def buscar(request):
    if request.GET['nombre_tipo']:
        tipo_de_cafe = request.GET['nombre_tipo']

        cafe = Tipos_de_cafe.objects.filter(nombre_tipo__icontains=tipo_de_cafe)

        return render(request, 'resultadobusqueda.html',{'cafe': cafe})
    
    else:
        respuesta = "No es un tipo de cafe"
        return render(request, 'busquedanegativa.html',{'cafe': respuesta})

def ingreso(request):
    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            clave = data["password"]

            user = authenticate(username=usuario, password=clave)

            if user:

                login(request, user)

                return render(request,'inicio.html', {"mensaje": f'Bienvenido {usuario}'})

            else:
                
                return render(request,'inicio.html', {"mensaje": 'Error, los datos ingresados son incorrectos'})
          
                
        return render(request,'inicio.html', {"mensaje": "Error, formulario invalido"})

    else:
        
        miFormulario = AuthenticationForm()
        
    return render(request, 'login.html', {'miFormulario': miFormulario})

def register(request):
    
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)

        if form.is_valid():

            usuario = form.cleaned_data["username"]

            form.save()

            return render(request, "inicio.html", {"mensaje": f'Usuario {usuario} creado exitosamente, Bienvenido.'})        

    else:

        form = RegistroUsuario()

    return render(request, "registro.html", {'miFormulario': form}) 

class cafes_DeleteView(DeleteView):
    model = Tipos_de_cafe
    template_name = "delete_cafe.html"
    success_url = '/app_STT/'

class cafes_DetailView(DetailView):
    model = Tipos_de_cafe
    template_name = "detail_cafe.html"
    context_object_name = 'cafe'


class cafes_UpdateView(UpdateView):
    model = Tipos_de_cafe
    template_name = "update_cafe.html"
    fields = ['nombre_tipo','ingredientes']
    success_url = '/app_STT/'


class usuario_DeleteView(DeleteView):
    model = User
    template_name = "delete_user.html"
    success_url = '/app_STT/'

class usuario_DetailView(DetailView):
    model = User
    template_name = "detail_user.html"
    context_object_name = 'user'


class perfil_DetailView(DetailView):
    model = User
    template_name = "perfil.html"
    context_object_name = 'user'

class usuario_UpdateView(UpdateView):
    model = User
    template_name = "update_user.html"
    fields = ['username','email']
    success_url = '/app_STT/'


