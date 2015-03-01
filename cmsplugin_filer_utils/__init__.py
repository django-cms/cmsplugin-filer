# -*- coding: utf-8 -*-
from django.db import models


class FilerPluginManager(models.Manager):
    def __init__(self, select_related=None):
        self._select_related = select_related
        super(FilerPluginManager, self).__init__()

    def get_queryset(self):
        qs = super(FilerPluginManager, self).get_queryset()
        if self._select_related:
            qs = qs.prefetch_related(*self._select_related)
        return qs
