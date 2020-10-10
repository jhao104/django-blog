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
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def slice_list(value, index):
    return value[index]


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    content = mark_safe(markdown.markdown(value,
                                          output_format='html5',
                                          extensions=[
                                              'markdown.extensions.extra',
                                              'markdown.extensions.fenced_code',
                                              'markdown.extensions.tables',
                                          ],
                                          safe_mode=True,
                                          enable_attributes=False))
    return content


@register.filter
def tag2string(value):
    """
    将Tag转换成string >'python,爬虫'
    :param value:
    :return:
    """
    return ','.join([each.get('tag_name', '') for each in value])


if __name__ == '__main__':
    pass
