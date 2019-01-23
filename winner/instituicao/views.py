from django.shortcuts import render

# Create your views here.
def instituto(request):
    return render(request, 'principal_base.html', {'title':'Pagina Inicial'})

def suporte(request):
    return render(request, 'instituicao/suporte.html', {'title':'Suporte'})