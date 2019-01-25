from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new', views.new),
    url(r'^edit', views.edit),
    url(r'^remove', views.remove),
    url(r'^schedule_new', views.schedule_new),
    ]
