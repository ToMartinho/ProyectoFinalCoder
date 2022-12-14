from django.urls import path
from app_STT.views import  agregar_avatar, agregar_bio, avatar_UpdateView, cafes_CreateView, perfil, tipos_de_cafe, inicio, ver_tipos_cafe, ver_lista_metodos, metodos,lista_usuarios, buscar, ingreso, register, cafes_DetailView, cafes_DeleteView, cafes_UpdateView, usuario_UpdateView, usuario_DeleteView, about
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
    path('borrarusuario/<pk>', usuario_DeleteView.as_view(), name = "deleteuser"),
    path('actualizarusuario/<pk>', usuario_UpdateView.as_view(), name = "updateuser"),
    path('actualizaravatar/<pk>/', avatar_UpdateView.as_view(), name = "perfilavatar"),
    path('actualizar_bio/',agregar_bio , name = "updatebio"),
    path('profile/', perfil, name = "perfil"),
    path('receta/', cafes_CreateView.as_view(), name = "receta"),
    path('about/', about, name = "about")
    

]

