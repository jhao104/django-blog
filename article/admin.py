from django.contrib import admin
from django.conf import settings

# Register your models here.

from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('title', 'category', 'author', 'date_time', 'view')
    list_filter = ('category', 'author')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
