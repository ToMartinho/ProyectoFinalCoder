from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from app_STT.models import avatar


class RegistroUsuario(UserCreationForm):

        email = forms.EmailField()

        class Meta:
                model = User
                fields = ['username','email']
                help_texts ={k:""for k in fields}

class avatarformulario(forms.ModelForm):

        class Meta:
                model=avatar
                fields=('imagen',)
