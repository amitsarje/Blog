from django.conf.urls import url
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    url(r'^detail/(?P<id>\d+)/$', views.posts_detail, name='detail'),
    url(r'^create/$', views.posts_create, name='create'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login1, name='login'),
    url(r'^logout/$', views.logout1, name='logout'),
    url(r'^scan/$', views.posts_scan, name='scan'),
    url(r'^update/(?P<id>\d+)/$', views.posts_update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.posts_delete, name='delete'),
    url(r'^$', views.posts_list, name='list'),

    
]
