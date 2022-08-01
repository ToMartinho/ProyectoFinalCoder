from django import forms


class UsuarioFormulario(forms.Form):
        nombre = forms.CharField(max_length=50)
        email = forms.EmailField(max_length=200)