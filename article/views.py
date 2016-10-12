# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from article.models import Article


# Create your views here.

def home(request):
    post_list = Article.objects.all()  # 获取全部文章
    return render(request, 'article/home.html', {"post_list": post_list})


def detail(request, id):
    post = get_object_or_404(Article, pk=id)
    return render(request, 'article/post.html', {"post": post})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/archives.html', {'post_list': post_list,
                                                     'error': False})


def aboutMe(request):
    return render(request, 'article/aboutme.html')


def searchTag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/tag.html', {"post_list": post_list})


def blogSearch(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'article/home.html')
        else:
            post_list = Article.objects.filter(title__contains=s)
            error = False
            if len(post_list) == 0:
                error = True
            return render(request, 'article/archives.html', {'error': error, 'post_list': post_list})

    return redirect('/')


