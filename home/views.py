from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import *
from datetime import datetime
from datetime import timedelta

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        cargo = request.user.last_name
        nome = request.user.get_short_name()
        hora =  datetime.now().strftime('%-H')
        if cargo == 'diretor':
            return render(request, 'home/home.html', {'title':'Home', 'nome':nome, 'hora':hora})
        elif cargo == 'recepcionista':
            return render(request, 'home/home1.html', {'title':'Home', 'nome':nome, 'hora':hora})
        elif cargo == 'professor':
            return render(request, 'home/home2.html', {'title':'Home', 'nome':nome, 'hora':hora})
        elif cargo == 'aluno':
            return render(request, 'home/home3.html', {'title':'Home', 'nome':nome, 'hora':hora})
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    else:
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    
    