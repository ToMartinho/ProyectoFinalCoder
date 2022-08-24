from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistroUsuario(UserCreationForm):

        email = forms.EmailField()
        contraseña1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
        contraseña2 = forms.CharField(label='repetir contraseña', widget=forms.PasswordInput)

        class Meta:
                model = User
                fields = ['username','email','contraseña1','contraseña2']
                help_texts ={k:""for k in fields}