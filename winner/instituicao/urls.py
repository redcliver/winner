from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.instituto),
    url(r'^course', views.cursos),
    url(r'^suporte', views.suporte),
    ]
