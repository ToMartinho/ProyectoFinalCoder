from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def lobby(request):
    #user = User.objects.filter(numbre_usuario = username)
    return render(request, 'chat/lobby.html')