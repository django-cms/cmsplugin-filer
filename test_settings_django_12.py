#-*- coding: utf-8 -*-
from test_settings import *
INSTALLED_APPS.pop('django.contrib.staticfiles')
INSTALLED_APPS.append('staticfiles',)
