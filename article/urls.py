# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls.py  
   Description :  
   Author :       JHao
   date：          2016/10/10
-------------------------------------------------
   Change Activity:
                   2016/10/10: 
-------------------------------------------------
"""
__author__ = 'JHao'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', 'article.views.archives', name='archives'),
    url(r'^aboutme/$', 'article.views.aboutMe', name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', 'article.views.searchTag', name='search_tag'),
    url(r'^search/$', 'article.views.blogSearch', name='search'),
]
