# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     custom_markdown.py  
   Description :  
   Author :       JHao
   date：          2016/10/11
-------------------------------------------------
   Change Activity:
                   2016/10/11: 
-------------------------------------------------
"""
__author__ = 'JHao'

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    return mark_safe(
        markdown.markdown(value, extensions=['markdown.extensions.fenced_code',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.tables',
                                             ],
                          safe_mode=True, enable_attributes=False))
