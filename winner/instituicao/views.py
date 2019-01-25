from django.shortcuts import render

# Create your views here.
def instituto(request):
    return render(request, 'instituicao/pagina_principal.html', {'title':'Pagina Inicial'})
def cursos(request):
    return render(request, 'instituicao/cursos.html', {'title':'Pagina Inicial'})

def suporte(request):
    return render(request, 'instituicao/suporte.html', {'title':'Suporte'})