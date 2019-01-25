from django.shortcuts import render
import datetime
from .models import colaborador
# Create your views here.
def new(request):
    if request.method == 'GET':
         return render(request, 'colaborador/novo.html', {'title':'Novo Colaborador'})
    if request.method == 'POST' and request.POST.get('nome') != None:
        name = request.POST.get('nome')
        telefone = request.POST.get('tel')
        celular = request.POST.get('cel')
        email = request.POST.get('mail')
        data_nasc = request.POST.get('data_nasc')
        cargo = request.POST.get('cargo')
        novo_colaborador = colaborador(nome=name, telefone=telefone, celular=celular, data_nasc = data_nasc, email=email, cargo=cargo)
        novo_colaborador.save()
        msg = name + " salvo com sucesso!"
        return render(request, 'colaborador/novo.html', {'title':'Novo Colaborador', 'msg':msg})

def search(request):
    colaboradores = colaborador.objects.all().order_by('nome')
    if request.method == 'POST' and request.POST.get('colaborador_id') != None:
        colaborador_id = request.POST.get('colaborador_id')
        colaborador_obj = colaborador.objects.get(id=colaborador_id)
        return render(request, 'colaborador/edita.html', {'title':'Editar Colaborador', 'colaborador_obj':colaborador_obj})
    return render(request, 'colaborador/busca_edita.html', {'title':'Selecionar Colaborador', 'colaboradores':colaboradores})

def save(request):
    if request.method == 'POST' and request.POST.get('colaborador_id') != None:
        colaborador_id = request.POST.get('colaborador_id')
        colaborador_obj = colaborador.objects.get(id=colaborador_id)
        nome = request.POST.get('nome')
        tel = request.POST.get('tel')
        cel = request.POST.get('cel')
        mail = request.POST.get('mail')
        data_nasc = request.POST.get('data_nasc')
        cargo = request.POST.get('cargo')
        colaborador_obj.nome = nome
        colaborador_obj.telefone = tel
        colaborador_obj.celular = cel
        colaborador_obj.email = mail
        colaborador_obj.data_nasc = data_nasc
        colaborador_obj.cargo = cargo
        colaborador_obj.save()
        msg = colaborador_obj.nome + " editado(a) com sucesso!"
        return render(request, 'colaborador/edita.html', {'title':'Editar Colaborador', 'colaborador_obj':colaborador_obj, 'msg':msg})

def detail(request):
    colaboradores = colaborador.objects.all().order_by('nome')
    if request.method == 'POST' and request.POST.get('colaborador_id') != None:
        colaborador_id = request.POST.get('colaborador_id')
        colaborador_obj = colaborador.objects.get(id=colaborador_id)
        return render(request, 'colaborador/visualizar.html', {'title':'Visualizar Colaborador', 'colaborador_obj':colaborador_obj})
    return render(request, 'colaborador/busca_visualiza.html', {'title':'Selecionar Colaborador', 'colaboradores':colaboradores})
