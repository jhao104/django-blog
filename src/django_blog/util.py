# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     util
   Description :
   Author :        JHao
   date：          2020/9/30
-------------------------------------------------
   Change Activity:
                   2020/9/30:
-------------------------------------------------
"""
__author__ = 'JHao'

from math import ceil


class PageInfo(object):

    def __init__(self, page, total, limit=8):
        """

        :param page: 页数
        :param total: 总条数
        :param limit: 每页条数
        """
        self._limit = limit
        self._total = total
        self._page = page
        self._index_start = (int(page) - 1) * int(limit)
        self._index_end = int(page) * int(limit)

    @property
    def index_start(self):
        return self._index_start

    @property
    def index_end(self):
        return self._index_end

    @property
    def current_page(self):
        return self._page

    @property
    def total_page(self):
        return ceil(self._total / self._limit)

    @property
    def total_number(self):
        return self._total
