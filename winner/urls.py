"""
Definition of urls for sistemas.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^', include('instituicao.urls')),
    url(r'^school/', include('instituicao.urls')),
    url(r'^sistema_login/', LoginView.as_view(template_name='sistema_login/login.html'), name="login"),
    url(r'^home/', include('home.urls')),
    url(r'^class/', include('aulas.urls')),
    url(r'^aluno/', include('home_aluno.urls')),
    url(r'^diretor/', include('home_diretor.urls')),
    url(r'^professor/', include('home_prof.urls')),
    url(r'^recepcao/', include('home_recepcao.urls')),
    url(r'^student/', include('aluno.urls')),
    url(r'^crew/', include('colaborador.urls')),
    url(r'^classroom/', include('classe.urls')),
    url(r'^group/', include('grupo.urls')),
    url(r'^logout$', LogoutView.as_view(template_name='sistema_login/login.html'), name="login"),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]
