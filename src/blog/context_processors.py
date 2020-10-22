# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     context_processors.py  
   Description :  
   Author :       JHao
   date：          2017/4/14
-------------------------------------------------
   Change Activity:
                   2017/4/14: 
-------------------------------------------------
"""
__author__ = 'JHao'

import importlib
from django_blog import blogroll
from blog.models import Category, Article, Tag, Comment


def sidebar(request):
    category_list = Category.objects.all()
    # 所有类型

    blog_top = Article.objects.all().values("id", "title", "view").order_by('-view')[0:6]
    # 文章排行

    tag_list = Tag.objects.all()
    # 标签

    comment = Comment.objects.all().order_by('-create_time')[0:6]
    # 评论

    importlib.reload(blogroll)
    # 友链

    return {
        'category_list': category_list,
        'blog_top': blog_top,
        'tag_list': tag_list,
        'comment_list': comment,
        'blogroll': blogroll.sites

    }


if __name__ == '__main__':
    pass
