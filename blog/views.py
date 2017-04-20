# -*- coding: utf-8 -*-
# Create your views here.

import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from blog.models import Article, Category, Comment


def Index(request):
    """
    博客首页
    :param request:
    :return:
    """
    article_list = Article.objects.all().order_by('-date_time')[0:5]
    return render(request, 'blog/index.html', {"html_title": u"Memory & Write",
                                               "article_list": article_list,
                                               "source_id": "index"})


def Articles(request, pk):
    """
    博客列表页面
    :param request:
    :param pk:
    :return:
    """
    pk = int(pk)
    if pk:
        category_object = get_object_or_404(Category, pk=pk)
        category = category_object.name
        article_list = Article.objects.filter(category_id=pk)
    else:
        # pk为0时表示全部
        article_list = Article.objects.all()  # 获取全部文章
        category = u''
    return render(request, 'blog/articles.html', {"article_list": article_list,
                                                  "category": category,
                                                  "html_title": "博客列表"})


def About(request):
    return render(request, 'blog/about.html', {"html_title": "关于"})


def archive(request):
    article_list = Article.objects.order_by('-date_time')
    return render(request, 'blog/archive.html', {"html_title": "归档", "article_list": article_list})


def Link(request):
    return render(request, 'blog/link.html', {"html_title": "链接"})


def Message(request):
    return render(request, 'blog/message_board.html', {"html_title": "留言",
                                                       "source_url": "http://www.spiderpy.cn/blog/message"})


@csrf_exempt
def GetComment(request):
    """
    接收网易云跟帖评论消息， post方式回推
    :param request:
    :return:
    """
    arg = request.POST
    data = arg.get('data')
    data = json.loads(data)[0]
    title = data.get('title')
    url = data.get('url')
    source_id = data.get('sourceId')
    comments = data.get('comments')[0]
    content = comments.get('content')
    user = comments.get('user').get('nickname')
    Comment(title=title, source_id=source_id, user_name=user, url=url, comment=content).save()
    return JsonResponse({"status": "ok"})


def detail(request, pk):
    """
    博文详情
    :param request:
    :param pk:
    :return:
    """
    article = get_object_or_404(Article, pk=pk)
    article.viewed()
    return render(request, 'blog/detail.html', {"html_title": article.title,
                                                "article": article})


def search(request):
    """
    搜索
    :param request:
    :return:
    """
    key = request.GET['key']
    article_list = Article.objects.filter(title__contains=key)
    return render(request, 'blog/search.html',
                  {"html_title": u"搜索'{}'".format(key), "article_list": article_list, "key": key})


def tag(request, name):
    """
    标签
    :param request:
    :param name
    :return:
    """
    article_list = Article.objects.filter(tag__tag_name=name)
    return render(request, 'blog/tag.html', {"html_title": u"{}标签".format(name),
                                             "article_list": article_list,
                                             "tag": name})