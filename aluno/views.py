from django.shortcuts import render
import datetime
from .models import aluno
# Create your views here.
def new_rec(request):
    if request.user.is_authenticated:
        cargo = request.user.last_name
        if cargo == 'recepcao':
            if request.method == 'POST' and request.POST.get('nome') != None:
                name = request.POST.get('nome')
                telefone = request.POST.get('tel')
                celular = request.POST.get('cel')
                email = request.POST.get('mail')
                data_nasc = request.POST.get('data_nasc')
                estado = request.POST.get('estado')
                novo_aluno = aluno(nome=name, telefone=telefone, celular=celular, data_nasc = data_nasc, email=email, estado=estado)
                novo_aluno.save()
                msg = name + " salvo com sucesso!"
                return render(request, 'aluno/novo_rec.html', {'title':'Novo Aluno', 'msg':msg})
            return render(request, 'aluno/novo_rec.html', {'title':'Novo Aluno'})
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    else:
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
         
    

def search_rec(request):
    if request.user.is_authenticated:
        cargo = request.user.last_name
        if cargo == 'recepcao':
            alunos = aluno.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('aluno_id') != None:
                aluno_id = request.POST.get('aluno_id')
                aluno_obj = aluno.objects.get(id=aluno_id)
                return render(request, 'aluno/edita_rec.html', {'title':'Editar Aluno', 'aluno_obj':aluno_obj})
            return render(request, 'aluno/busca_edita_rec.html', {'title':'Selecionar Aluno', 'alunos':alunos})
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    else:
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})

def save_rec(request):
    if request.user.is_authenticated:
        cargo = request.user.last_name
        if cargo == 'recepcao':
            if request.method == 'POST' and request.POST.get('aluno_id') != None:
                aluno_id = request.POST.get('aluno_id')
                aluno_obj = aluno.objects.get(id=aluno_id)
                nome = request.POST.get('nome')
                tel = request.POST.get('tel')
                cel = request.POST.get('cel')
                mail = request.POST.get('mail')
                data_nasc = request.POST.get('data_nasc')
                estado = request.POST.get('estado')
                aluno_obj.nome = nome
                aluno_obj.telefone = tel
                aluno_obj.celular = cel
                aluno_obj.email = mail
                aluno_obj.data_nasc = data_nasc
                aluno_obj.estado = estado
                aluno_obj.save()
                msg = aluno_obj.nome + " editado(a) com sucesso!"
                return render(request, 'aluno/edita_rec.html', {'title':'Editar Aluno', 'aluno_obj':aluno_obj, 'msg':msg})
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    else:
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})

def detail_rec(request):
    if request.user.is_authenticated:
        cargo = request.user.last_name
        if cargo == 'recepcao':
            alunos = aluno.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('aluno_id') != None:
                aluno_id = request.POST.get('aluno_id')
                aluno_obj = aluno.objects.get(id=aluno_id)
                return render(request, 'aluno/visualizar_rec.html', {'title':'Visualizar Aluno', 'aluno_obj':aluno_obj})
            return render(request, 'aluno/busca_visualiza_rec.html', {'title':'Selecionar Aluno', 'alunos':alunos})
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    else:
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
