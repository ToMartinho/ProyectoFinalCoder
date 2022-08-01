from django.urls import path
from app_STT.views import tipos_de_cafe, inicio, ver_tipos_cafe, ver_lista_metodos, metodos

urlpatterns = [
    path('index/', inicio, name= "Inicio"),
    path('TiposDeCafe/', tipos_de_cafe, name = "TiposDeCafe"),
    path('CafeLista/', ver_tipos_cafe, name = "listaDeCafes"),
    path('MetodosLista/', ver_lista_metodos, name = "listaMetodos"),
    path('MetodosDeCafe/', metodos, name = "MetodosDeCafe"),
]

