# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     context_processors.py  
   Description :  
   Author :       JHao
   date：          2016/11/19
-------------------------------------------------
   Change Activity:
                   2016/11/19: 
-------------------------------------------------
"""

from django.db.models import Count
from .models import Article, Category


# def sidebar(request):
#     rank_article = Article.objects.order_by("-view")[0:7]
#     category = Category.objects.all()
#     return {
#         "rank_article": rank_article,
#         "category": category,
#     }


def sidebar(request):
    article = Article.objects.all().order_by("-view")
    article_list = article[:]
    rank_article = article_list[0:7]
    stat_dict = dict()
    pk_dict = dict()
    for tag in article_list:
        stat_dict[tag.category.name] = stat_dict.get(tag.category.name, 0) + 1
        pk_dict[tag.category.name] = tag.category_id
    category = [{'pk': pk_dict.get(name), 'name': name, 'count': stat_dict.get(name, 0)} for name in stat_dict]
    return {
        "rank_article": rank_article,
        "category": category,
    }
