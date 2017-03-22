# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views.py  
   Description :  
   Author :       JHao
   date：          2016/11/18
-------------------------------------------------
   Change Activity:
                   2016/11/18: 
-------------------------------------------------
"""

# -*- coding: UTF-8 -*-

from django.shortcuts import render, get_object_or_404, redirect, render_to_response
# from django.http import Http404, HttpResponse

from article.models import Article


# Create your views here.

def home(request):
    post_list = Article.objects.all()  # 获取全部文章
    return render(request, 'article/articles.html', {"post_list": post_list,
                                                     "title": "j_hao104's blog"})


def detail(request, id):
    post = get_object_or_404(Article, pk=id)
    post.viewed()
    return render(request, 'article/article.html', {"post": post,
                                                    "title": post.title})


def category(request, id):
    post_list = Article.objects.filter(category_id=id)
    return render(request, 'article/articles.html', {"post_list": post_list,
                                                     "title": "j_hao104's blog"})


def archives(request):
    post_list = Article.objects.order_by('-date_time')
    post_dict = dict()
    count = 0
    for post in post_list:
        count += 1
        date_time = post.date_time
        year = date_time.strftime('%Y')
        day = date_time.strftime('%m.%d')
        post_dict[year] = post_dict.get(year, list()) + [{'day': day, 'title': post.title, 'id': post.id}]
    post_dict = sorted(post_dict.iteritems(), key=lambda d: d[0], reverse=True)
    return render(request, 'article/archives.html', {"title": "j_hao104's blog",
                                                     'count': count,
                                                     "post_dict": post_dict})
