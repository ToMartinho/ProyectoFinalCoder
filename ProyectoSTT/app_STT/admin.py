from django.contrib import admin

from app_STT.models import  Metodo, Perfil, Tipos_de_cafe

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Tipos_de_cafe)
admin.site.register(Metodo)
