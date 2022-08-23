from django.urls import path
from app_STT.views import tipos_de_cafe, inicio, ver_tipos_cafe, ver_lista_metodos, metodos, lista_usuarios, crea_usuario, buscar, ingreso, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('TiposDeCafe/', tipos_de_cafe, name = "TiposDeCafe"),
    path('CafeLista/', ver_tipos_cafe, name = "listaDeCafes"),
    path('MetodosLista/', ver_lista_metodos, name = "listaMetodos"),
    path('MetodosDeCafe/', metodos, name = "MetodosDeCafe"),
    path('ListaUsuarios/', lista_usuarios, name = "ListaUsuarios"),
    path('creausuario/', crea_usuario, name = "creausuario"),
    path('buscar/', buscar, name = "buscar"),
    path('login/', ingreso, name = "Login"),
    path('registrar/', register, name = "Registrar"),
    path('deslog/', LogoutView.as_view(template_name="logout.html"), name = "Deslog"),
]

