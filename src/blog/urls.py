# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls.py  
   Description :  
   Author :       JHao
   date：          2017/4/13
-------------------------------------------------
   Change Activity:
                   2017/4/13: 
-------------------------------------------------
"""
__author__ = 'JHao'

from blog import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.blog_list, name='list'),
    path('detail/<int:blog_id>$', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('archive/', views.archive, name='archive'),
    path('link/', views.link, name='link'),
    path('message/', views.message, name='message'),
    path('article/<int:article_id>/', views.articles, name='article'),
    path(r'^getComment/$', views.getComment, name='get_comment'),
    path(r'^search/$', views.search, name='search'),
    path(r'^tag/(?P<name>.*?)/$', views.tag, name='tag'),

]
