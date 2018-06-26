from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.con_list, name='con_list'),
    url(r'^addr/(?P<pk>\d+)/$', views.con_detail, name='con_detail'),
    url(r'^addr/new/$', views.con_new, name='con_new'),
    url(r'^addr/(?P<pk>\d+)/edit$', views.con_edit, name='con_edit'),
]