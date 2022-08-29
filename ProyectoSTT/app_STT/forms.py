from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

from app_STT.models import Perfil


class RegistroUsuario(UserCreationForm):

        email = forms.EmailField()

        class Meta:
                model = User
                fields = ['username','email']
                help_texts ={k:""for k in fields}

class AvatarFormulario(forms.Form):
        imagen = forms.ImageField()
        class Meta:
                model= Perfil
                fields = ['imagen']

class BioFormulario(forms.Form):
        bio = forms.CharField(required=False, widget=forms.Textarea)
        link = forms.URLField(required=False)
        class Meta:
                model=Perfil
                fields = ['bio','link']

