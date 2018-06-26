from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.con_list, name='con_list'),
    url(r'^addr/(?P<pk>\d+)/$', views.con_detail, name='con_detail'),
    url(r'^addr/(?P<pk>\d+)/edit/$', views.con_edit, name='con_edit'),
    url(r'^addr/(?P<pk>\d+)/publish/$', views.con_publish, name='con_publish'),
    url(r'^addr/(?P<pk>\d+)/remove/$', views.con_remove, name='con_remove'),
    url(r'^addr/(?P<pk>\d+)/secret$', views.con_secret_addr, name='con_secret_addr'),
    url(r'^addr/(?P<pk>\d+)/memo/$', views.con_memo_new, name='con_memo_new'),
    url(r'^addr/new/$', views.con_new, name='con_new'),
    url(r'^drafts/$', views.con_draft_list, name='con_draft_list'),
]