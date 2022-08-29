from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app_STT.models import Perfil, Tipos_de_cafe


class RegistroUsuario(UserCreationForm):

        email = forms.EmailField()

        class Meta:
                model = User
                fields = ['username','email']
                help_texts ={k:""for k in fields}

class AvatarFormulario(forms.ModelForm):
        class Meta:
                model= Perfil
                fields = ['imagen']

class BioFormulario(forms.ModelForm):
        bio = forms.CharField(required=False, widget=forms.Textarea)
        link = forms.URLField(required=False)
        class Meta:
                model=Perfil
                fields = ['bio','link']

class RecetaFormulario(forms.ModelForm):
        class Meta:
                model=Tipos_de_cafe
                fields = '__all__'
                exclude = ['user']