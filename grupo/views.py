from django.shortcuts import render
from classe.models import aluno, grupo_aula, sala_aula, aula, presenca
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

def schedule_new(request):
    grupos = grupo_aula.objects.all().order_by('nome')
    professores = colaborador.objects.filter(cargo=2).all().order_by('nome')
    classes = sala_aula.objects.all().order_by('nome')
    if request.method == 'POST':
        data = request.POST.get('data')
        grupo_id = request.POST.get('grupo_id')
        classe_id = request.POST.get('classe_id')
        professor_id = request.POST.get('professor_id')
        grupo_obj = grupo_aula.objects.filter(id=grupo_id).get()
        classe_obj = sala_aula.objects.filter(id=classe_id).get()
        professor_obj = colaborador.objects.filter(id=professor_id).get()
        un = classe_obj.unidade
        nova_aula = aula(unidade=un, group=grupo_obj, pro=professor_obj, classe=classe_obj, data_aula=data)
        nova_aula.save()
        for a in  grupo_obj.alunos.all():
            nova_presenca = presenca(student=a)
            nova_presenca.save()
            nova_aula.presentes.add(nova_presenca)
            nova_aula.save()
        dat = parse_datetime(data)
        msg = str(dat.strftime('%d/%m/%Y')) + " ás " + str(dat.strftime('%H:%M')) + " agendada com sucesso."
        grupos = grupo_aula.objects.all().order_by('nome')
        professores = colaborador.objects.filter(cargo=2).all().order_by('nome')
        classes = sala_aula.objects.all().order_by('nome')
        return render(request, 'grupo/aula_novo.html', {'title':'Nova Aula', 'grupos':grupos, 'professores':professores, 'classes':classes, 'msg':msg})
    return render(request, 'grupo/aula_novo.html', {'title':'Nova Aula', 'grupos':grupos, 'professores':professores, 'classes':classes})

def schedule_search(request):
    data_inicio = datetime.now() + timedelta(days=-1)
    data_inicio = data_inicio.strftime('%Y-%m-%d')
    data_fim = datetime.now().strftime('%Y-%m-%d')
    aulas_all = aula.objects.filter(data_aula__date=(data_fim)).all().order_by('data_aula')
    if request.method == 'POST' and request.POST.get('data_inicio') != None and request.POST.get('data_fim') != None:
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        aulas_all = aula.objects.filter(data_aula__range=(data_inicio,data_fim)).all().order_by('data_aula')
        return render(request, 'grupo/aula_busca.html', {'title':'Selecione a Aula', 'aulas_all':aulas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})
    return render(request, 'grupo/aula_busca.html', {'title':'Selecione a Aula', 'aulas_all':aulas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})

def schedule_detail(request):
    data_inicio = datetime.now() + timedelta(days=-1)
    data_inicio = data_inicio.strftime('%Y-%m-%d')
    data_fim = datetime.now().strftime('%Y-%m-%d')
    aulas_all = aula.objects.filter(data_aula__date=(data_fim)).all().order_by('data_aula')
    if request.method == 'POST' and request.POST.get('aula_id') != None:
        aula_id = request.POST.get('aula_id')
        data_fim = request.POST.get('data_fim')
        aula_obj = aula.objects.filter(id=aula_id).get()
        grupo_id = aula_obj.group.id
        grupo_obj = grupo_aula.objects.filter(id=grupo_id).get()
        alunos_grupo = grupo_obj.alunos.all().order_by('nome')
        return render(request, 'grupo/aula_visualizar.html', {'title':'Visualizar Aula', 'aula_obj':aula_obj, 'alunos_grupo':alunos_grupo})
    return render(request, 'grupo/aula_busca.html', {'title':'Selecione a Aula', 'aulas_all':aulas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})

def schedule_edit(request):
    data_inicio = datetime.now() + timedelta(days=-1)
    data_inicio = data_inicio.strftime('%Y-%m-%d')
    data_fim = datetime.now().strftime('%Y-%m-%d')
    aulas_all = aula.objects.filter(data_aula__date=(data_fim)).all().order_by('data_aula')
    if request.method == 'POST' and request.POST.get('aula_id') != None:
        aula_id = request.POST.get('aula_id')
        aula_obj = aula.objects.filter(id=aula_id).get()
        grupo_id = aula_obj.group.id
        prof_id = aula_obj.pro.id
        classe_id = aula_obj.classe.id
        grupo_obj = grupo_aula.objects.filter(id=grupo_id).get()
        alunos_grupo = grupo_obj.alunos.all().order_by('nome')
        grupos = grupo_aula.objects.all().order_by('nome')
        grupos = grupos.exclude(id=grupo_id)
        professores = colaborador.objects.filter(cargo=2).all().order_by('nome')
        professores = professores.exclude(id=prof_id)
        classes = sala_aula.objects.all().order_by('nome')
        classes = classes.exclude(id=classe_id)
        return render(request, 'grupo/aula_edita.html', {'title':'Editar Aula', 'aula_obj':aula_obj, 'alunos_grupo':alunos_grupo, 'grupos':grupos, 'professores':professores, 'classes':classes})
    return render(request, 'grupo/aula_busca_edita.html', {'title':'Selecione a Aula', 'aulas_all':aulas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})

def schedule_save(request):
    if request.method == 'POST' and request.POST.get('aula_id') != None:
        aula_id = request.POST.get('aula_id')
        nova_data = request.POST.get('nova_data')
        estado = request.POST.get('estado')
        grupo_id = request.POST.get('grupo_id')
        classe_id = request.POST.get('classe_id')
        professor_id = request.POST.get('professor_id')
        grupo_obj = grupo_aula.objects.filter(id=grupo_id).get()
        classe_obj = sala_aula.objects.filter(id=classe_id).get()
        professor_obj = colaborador.objects.filter(id=professor_id).get()
        un = classe_obj.unidade
        aula_obj = aula.objects.filter(id=aula_id).get()
        aula_obj.estado = estado
        aula_obj.group = grupo_obj
        aula_obj.pro = professor_obj
        aula_obj.classe = classe_obj
        aula_obj.unidade = un
        aula_obj.save()
        if nova_data != '':
            aula_obj.data_aula = nova_data
            aula_obj.save()
            if nova_data != None:
                aula_obj.data_aula = nova_data
                aula_obj.save()
        
        grupo_id = aula_obj.group.id
        prof_id = aula_obj.pro.id
        classe_id = aula_obj.classe.id
        grupo_obj = grupo_aula.objects.filter(id=grupo_id).get()
        alunos_grupo = grupo_obj.alunos.all().order_by('nome')
        grupos = grupo_aula.objects.all().order_by('nome')
        grupos = grupos.exclude(id=grupo_id)
        professores = colaborador.objects.filter(cargo=2).all().order_by('nome')
        professores = professores.exclude(id=prof_id)
        classes = sala_aula.objects.all().order_by('nome')
        classes = classes.exclude(id=classe_id)
        return render(request, 'grupo/aula_edita.html', {'title':'Editar Aula', 'aula_obj':aula_obj, 'alunos_grupo':alunos_grupo, 'grupos':grupos, 'professores':professores, 'classes':classes})
    return render(request, 'grupo/aula_edita.html', {'title':'Editar Aula', 'aula_obj':aula_obj, 'alunos_grupo':alunos_grupo})
