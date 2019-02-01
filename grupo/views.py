from django.shortcuts import render
from classe.models import aluno, grupo_aula, sala_aula
from aulas.models import aula, presenca
from colaborador.models import colaborador
from django.utils import timezone
import datetime
from datetime import datetime
from datetime import timedelta, date
from django.utils.dateparse import parse_datetime

# Create your views here.
def new(request):
    if request.method == 'POST' and request.POST.get('nome') != None :
        nome = request.POST.get('nome')
        unidade = request.POST.get('unidade')
        livro = request.POST.get('livro')
        pagina = request.POST.get('pagina')
        obs = request.POST.get('obs')
        novo_grupo = grupo_aula(nome=nome, livro=livro, unidade=unidade, pag_atual=pagina, obs=obs)
        novo_grupo.save()
        alunos = aluno.objects.filter(estado=1).all().order_by('nome')
        msg = novo_grupo.nome + " criado com sucesso."
        return render(request, 'grupo/edita_grupo.html', {'title':'Editar Grupo', 'alunos':alunos, 'grupo_obj':novo_grupo, 'msg':msg})
    return render(request, 'grupo/novo_grupo.html', {'title':'Novo Grupo'})

def edit(request):
    grupos = grupo_aula.objects.all().order_by('nome')
    if request.method == 'POST' and request.POST.get('grupo_id') != None and request.POST.get('aluno_id') == None:
        grupo_id = request.POST.get('grupo_id')
        grupo_obj = grupo_aula.objects.filter(id=grupo_id).get()
        alunos = aluno.objects.filter(estado=1).all().order_by('nome')
        for a in grupo_obj.alunos.all():
            identificacao = a.id
            alunos.exclude(id=identificacao)
        alunos_grupo = grupo_obj.alunos.all().order_by('nome')
        return render(request, 'grupo/edita_grupo.html', {'title':'Editar Grupo', 'alunos':alunos, 'grupo_obj':grupo_obj, 'alunos_grupo':alunos_grupo})
    if request.method == 'POST' and request.POST.get('grupo_id') != None and request.POST.get('aluno_id') != None:
        grupo_id = request.POST.get('grupo_id')
        aluno_id = request.POST.get('aluno_id')
        grupo_obj = grupo_aula.objects.filter(id=grupo_id).get()
        aluno_obj = aluno.objects.filter(id=aluno_id).get()
        grupo_obj.alunos.add(aluno_obj)
        grupo_obj.save()
        alunos_obj1 = aluno.objects.filter(estado=1).all().order_by('nome')
        for a in grupo_obj.alunos.all():
            identificacao = a.id
            alunos_obj1.exclude(id=identificacao)
        alunos_grupo = grupo_obj.alunos.all().order_by('nome')
        return render(request, 'grupo/edita_grupo.html', {'title':'Editar Grupo', 'alunos':alunos_obj1, 'grupo_obj':grupo_obj, 'alunos_grupo':alunos_grupo})
    return render(request, 'grupo/busca_edita.html', {'title':'Editar Grupo', 'grupos':grupos})

def remove(request):
    if request.method == 'POST' and request.POST.get('grupo_id') != None and request.POST.get('aluno_id') != None:
        grupo_id = request.POST.get('grupo_id')
        aluno_id = request.POST.get('aluno_id')
        grupo_obj = grupo_aula.objects.filter(id=grupo_id).get()
        aluno_obj = aluno.objects.filter(id=aluno_id).get()
        alunos_obj1 = aluno.objects.filter(estado=1).all().order_by('nome')
        for a in grupo_obj.alunos.all():
            alunos_obj1.exclude(id=a.id)
        grupo_obj.alunos.remove(aluno_obj)
        grupo_obj.save()
        alunos_grupo = grupo_obj.alunos.all().order_by('nome')
        msg = aluno_obj.nome + " removido com sucesso."
        return render(request, 'grupo/edita_grupo.html', {'title':'Editar Grupo', 'alunos':alunos_obj1, 'grupo_obj':grupo_obj, 'alunos_grupo':alunos_grupo, 'msg':msg})
    return render(request, 'grupo/busca_edita.html', {'title':'Editar Grupo', 'grupos':grupos})


