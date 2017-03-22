# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     models.py  
   Description :  
   Author :       JHao
   date：          2016/11/18
-------------------------------------------------
   Change Activity:
                   2016/11/18: 
-------------------------------------------------
"""

# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=200)  # 博客标题
    category = models.ForeignKey('Category', verbose_name=u'标签', on_delete=models.CASCADE)
    date_time = models.DateField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客正文
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'作者', on_delete=models.CASCADE)
    view = models.BigIntegerField(default=0)  # pv
    comment = models.BigIntegerField(default=0)  # 评论
    like = models.BigIntegerField(default=0)  # 喜欢 or 点赞
    classify = models.CharField(max_length=100)  # 分类

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        path = reverse('article:detail', kwargs={'id': self.id})
        return "http://www.spiderpy.cn%s" % path  # 给多说使用

    def viewed(self):
        self.view += 1
        self.save(update_fields=['view'])

    class Meta:  # 按时间降序
        ordering = ['-date_time']


class Category(models.Model):
    name = models.CharField(u'标签', max_length=30)
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
