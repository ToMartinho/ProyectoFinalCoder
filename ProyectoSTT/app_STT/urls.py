from django.urls import path
from app_STT.views import tipos_de_cafe, inicio, ver_tipos_cafe, ver_lista_metodos, metodos,lista_usuarios, buscar, ingreso, register, cafes_DetailView, cafes_DeleteView, cafes_UpdateView, usuario_UpdateView, usuario_DetailView, usuario_DeleteView,perfil_DetailView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('TiposDeCafe/', tipos_de_cafe, name = "TiposDeCafe"),
    path('CafeLista/', ver_tipos_cafe, name = "listaDeCafes"),
    path('MetodosLista/', ver_lista_metodos, name = "listaMetodos"),
    path('MetodosDeCafe/', metodos, name = "MetodosDeCafe"),
    path('ListaUsuarios/', lista_usuarios, name = "ListaUsuarios"),
    path('buscar/', buscar, name = "buscar"),
    path('login/', ingreso, name = "Login"),
    path('registrar/', register, name = "Registrar"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name = "Deslog"),
    path('detallecafe/<pk>', cafes_DetailView.as_view(), name = "detailcafe"),
    path('borrarcafe/<pk>', cafes_DeleteView.as_view(), name = "deletecafe"),
    path('actualizarcafe/<pk>', cafes_UpdateView.as_view(), name = "updatecafe"),
    path('borrarusuario/', usuario_DeleteView.as_view(), name = "deleteuser"),
    path('actualizarusuario/', usuario_UpdateView.as_view(), name = "updateuser"),
    path('perfilusuario/<pk>', usuario_DetailView.as_view(), name = "detailuser"),
    path('profile/', perfil_DetailView.as_view(), name = "perfil"),

]

