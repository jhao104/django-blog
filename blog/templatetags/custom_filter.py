# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     custom_filter.py  
   Description :  
   Author :       JHao
   date：          2017/4/14
-------------------------------------------------
   Change Activity:
                   2017/4/14: 
-------------------------------------------------
"""
__author__ = 'JHao'

import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def slice_list(value, index):
    return value[index]


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown.markdown(value, extensions=['markdown.extensions.fenced_code',
                                                          'markdown.extensions.codehilite',
                                                          'markdown.extensions.tables'],
                                       safe_mode=True, enable_attributes=False))


@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
    context['count'] = object_list.count
    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')

    try:
        object_list = paginator.page(page)
        context['current_page'] = int(page)

    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages

    context['article_list'] = object_list
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1
    return ''  # 必须加这个，否则首页会显示个None


@register.filter
def tag2string(value):
    """
    将Tag转换成string >'python,爬虫'
    :param value:
    :return:
    """
    return ','.join([each.get('tag_name', '') for each in value])


@register.filter
def getTag(value):
    """
    展示一个tag
    :param value:
    :return:
    """
    tag = ''
    for each in value:
        if each.get('tag_name'):
            tag = each.get("tag_name")
            break
    return tag


if __name__ == '__main__':
    pass
