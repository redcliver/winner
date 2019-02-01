from django.shortcuts import render
from classe.models import aluno, grupo_aula, sala_aula
from aulas.models import aula, presenca
from colaborador.models import colaborador
from django.utils import timezone
import datetime
from datetime import datetime
from datetime import timedelta, date
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User

# Create your views here.
def schedule_new_rec(request):
    if request.user.is_authenticated:
        cargo = request.user.last_name
        if cargo == 'professor' or cargo == 'recepcao' or cargo == 'diretor':
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
                return render(request, 'aulas/aula_novo_rec.html', {'title':'Nova Aula', 'grupos':grupos, 'professores':professores, 'classes':classes, 'msg':msg})
            return render(request, 'aulas/aula_novo_rec.html', {'title':'Nova Aula', 'grupos':grupos, 'professores':professores, 'classes':classes})
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})
    else:
        return render(request, 'sistema_login/login.html', {'title':'Entrar'})

def schedule_search_rec(request):
    data_inicio = datetime.now() + timedelta(days=-1)
    data_inicio = data_inicio.strftime('%Y-%m-%d')
    data_fim = datetime.now().strftime('%Y-%m-%d')
    aulas_all = aula.objects.filter(data_aula__date=(data_fim)).all().order_by('data_aula')
    if request.method == 'POST' and request.POST.get('data_inicio') != None and request.POST.get('data_fim') != None:
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        aulas_all = aula.objects.filter(data_aula__range=(data_inicio,data_fim)).all().order_by('data_aula')
        return render(request, 'aulas/aula_busca_rec.html', {'title':'Selecione a Aula', 'aulas_all':aulas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})
    return render(request, 'aulas/aula_busca_rec.html', {'title':'Selecione a Aula', 'aulas_all':aulas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})

def schedule_detail_rec(request):
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
        return render(request, 'aulas/aula_visualizar_rec.html', {'title':'Visualizar Aula', 'aula_obj':aula_obj, 'alunos_grupo':alunos_grupo})
    return render(request, 'aulas/aula_busca_rec.html', {'title':'Selecione a Aula', 'aulas_all':aulas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})

def schedule_edit_rec(request):
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
        return render(request, 'aulas/aula_edita_rec.html', {'title':'Editar Aula', 'aula_obj':aula_obj, 'alunos_grupo':alunos_grupo, 'grupos':grupos, 'professores':professores, 'classes':classes})
    return render(request, 'aulas/aula_busca_edita_rec.html', {'title':'Selecione a Aula', 'aulas_all':aulas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})

def schedule_save_rec(request):
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
        return render(request, 'aulas/aula_edita_rec.html', {'title':'Editar Aula', 'aula_obj':aula_obj, 'alunos_grupo':alunos_grupo, 'grupos':grupos, 'professores':professores, 'classes':classes})
    return render(request, 'aulas/aula_edita_rec.html', {'title':'Editar Aula', 'aula_obj':aula_obj, 'alunos_grupo':alunos_grupo})

