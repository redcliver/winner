from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from decimal import *
from datetime import datetime
from datetime import timedelta

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        cargo = request.user.last_name
        nome = request.user.get_short_name().split(' ', 1)[0] 
        hora =  datetime.now().strftime('%H')
        if cargo == 'diretor':
            return render(request, 'home_diretor/home_diretor.html', {'title':'Home', 'nome':nome, 'hora':hora})
        elif cargo == 'recepcao':
            return render(request, 'home_recepcao/home_recepcao.html', {'title':'Home', 'nome':nome, 'hora':hora})
        elif cargo == 'professor':
            return render(request, 'home_prof/home_prof.html', {'title':'Home', 'nome':nome, 'hora':hora})
        elif cargo == 'aluno':
            return render(request, 'home_aluno/home_aluno.html', {'title':'Home', 'nome':nome, 'hora':hora})
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    else:
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    