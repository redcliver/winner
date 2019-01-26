from django.shortcuts import render
# Create your views here.
def sistema_login(request):
    return render(request, 'sistema_login/login.html', {'title':'Login'})