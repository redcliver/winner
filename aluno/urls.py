from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new_rec', views.new_rec),
    url(r'^search_rec', views.search_rec),
    url(r'^save_rec', views.save_rec),
    url(r'^detail_rec', views.detail_rec),
    ]
