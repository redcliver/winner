"""
Definition of urls for winner.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

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
    url(r'^sistema_login/', include('sistema_login.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^student/', include('aluno.urls')),
    url(r'^crew/', include('colaborador.urls')),
    url(r'^class/', include('classe.urls')),
    url(r'^group/', include('grupo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
]
