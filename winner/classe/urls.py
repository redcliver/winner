from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new', views.new),
    url(r'^edit', views.edit),
    url(r'^detail', views.detail),
    ]
