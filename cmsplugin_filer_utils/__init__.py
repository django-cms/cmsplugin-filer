# -*- coding: utf-8 -*-
from django.db import models


class FilerPluginManager(models.Manager):
    def __init__(self, select_related=None):
        self._select_related = select_related
        super(FilerPluginManager, self).__init__()

    def get_queryset(self):
        # Remove once support for Django 1.4/1.5 are dropped
        try:
            qs = super(FilerPluginManager, self).get_queryset()
        except AttributeError:
            qs = super(FilerPluginManager, self).get_query_set()
        if self._select_related:
            qs = qs.prefetch_related(*self._select_related)
        return qs

    get_query_set = get_queryset
