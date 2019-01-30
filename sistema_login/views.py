from django.shortcuts import render
# Create your views here.
def sistema_login(request):
    if request.user.is_authenticated():
        cargo = request.user.last_name
        nome = cargo = request.user.first_name
        if cargo == 'diretor':
            return render(request, 'home/home.html', {'title':'Home', 'nome':nome})
        elif cargo == 'recepcionista':
            return render(request, 'home/home1.html', {'title':'Home', 'nome':nome})
        elif cargo == 'professor':
            return render(request, 'home/home2.html', {'title':'Home', 'nome':nome})
        elif cargo == 'aluno':
            return render(request, 'home/home3.html', {'title':'Home', 'nome':nome})
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    else:
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})