#-*- coding: utf-8 -*-
from django.conf import settings
from appconf import AppConf


class CmspluginFilerImageAppConf(AppConf):
    STYLE_CHOICES = (
        ('default', 'Default'),
    )
