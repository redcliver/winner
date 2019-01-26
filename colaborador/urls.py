from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new', views.new),
    url(r'^search', views.search),
    url(r'^save', views.save),
    url(r'^detail', views.detail),
    ]
