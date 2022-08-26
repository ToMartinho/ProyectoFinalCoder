from django.contrib import admin

from app_STT.models import Metodo, Tipos_de_cafe, avatar

# Register your models here.
admin.site.register(avatar)
admin.site.register(Tipos_de_cafe)
admin.site.register(Metodo)