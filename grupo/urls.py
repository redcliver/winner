from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new', views.new),
    url(r'^edit', views.edit),
    url(r'^remove', views.remove),
    url(r'^schedule_new', views.schedule_new),
    url(r'^schedule_search', views.schedule_search),
    url(r'^schedule_detail', views.schedule_detail),
    url(r'^schedule_edit', views.schedule_edit),
    url(r'^schedule_save', views.schedule_save),
    ]
