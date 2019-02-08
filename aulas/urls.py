from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^schedule_new_rec', views.schedule_new_rec),
    url(r'^schedule_search_rec', views.schedule_search_rec),
    url(r'^schedule_search_pro', views.schedule_search_pro),
    url(r'^schedule_detail_rec', views.schedule_detail_rec),
    url(r'^schedule_detail_pro', views.schedule_detail_pro),
    url(r'^schedule_edit_rec', views.schedule_edit_rec),
    url(r'^schedule_save_rec', views.schedule_save_rec),
    ]
