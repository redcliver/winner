from django.shortcuts import render
import datetime
from .models import sala_aula

# Create your views here.
def new(request):
    if request.method == 'POST' and request.POST.get('nome') != None:
        nome = request.POST.get('nome')
        unidade = request.POST.get('unidade')
        max_alunos = request.POST.get('max_alunos')
        obs = request.POST.get('obs')
        nova_sala = sala_aula(nome=nome, unidade=unidade, max_alunos=max_alunos, obs=obs)
        nova_sala.save()
        msg = nova_sala.nome + " cadastrada com sucesso."
        return render(request, 'classe/nova_classe.html', {'title':'Nova Classe', 'msg':msg})
    return render(request, 'classe/nova_classe.html', {'title':'Nova Classe'})

def edit(request):
    classes = sala_aula.objects.all().order_by('nome')
    if request.method == 'POST' and request.POST.get('classe_id') != None and request.POST.get('nome') == None:
        classe_id = request.POST.get('classe_id')
        classe_obj = sala_aula.objects.filter(id=classe_id).get()
        return render(request, 'classe/edita_classe.html', {'title':'Editar Classe', 'classe_obj':classe_obj})
    if request.method == 'POST' and request.POST.get('classe_id') != None and request.POST.get('nome') != None:
        classe_id = request.POST.get('classe_id')
        classe_obj = sala_aula.objects.filter(id=classe_id).get()
        nome = request.POST.get('nome')
        unidade = request.POST.get('unidade')
        max_alunos = request.POST.get('max_alunos')
        obs = request.POST.get('obs')
        classe_obj.nome = nome
        classe_obj.unidade = unidade
        classe_obj.max_alunos = max_alunos
        classe_obj.obs = obs
        classe_obj.save()
        msg = classe_obj.nome + " alterada com sucesso."
        classes = sala_aula.objects.all().order_by('nome')
        return render(request, 'classe/busca_edita.html', {'title':'Editar Classe', 'classes':classes, 'msg':msg})
    return render(request, 'classe/busca_edita.html', {'title':'Editar Classe', 'classes':classes})

def detail(request):
    classes = sala_aula.objects.all().order_by('nome')
    if request.method == 'POST' and request.POST.get('classe_id') != None and request.POST.get('nome') == None:
        classe_id = request.POST.get('classe_id')
        classe_obj = sala_aula.objects.filter(id=classe_id).get()
        return render(request, 'classe/visualiza_classe.html', {'title':'Visualizar Classe', 'classe_obj':classe_obj})
    return render(request, 'classe/busca_visualiza.html', {'title':'Visualizar Classe', 'classes':classes})