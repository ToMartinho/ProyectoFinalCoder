from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lobby(request):
    user = User.objects.all()
    return render(request, 'chat/lobby.html',{'username': user})