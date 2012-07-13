# -*- coding: utf-8 -*-
from django.template import Library
#TODO: Remove this templatetag entirely when the minimum supported Django-CMS version will be moved to 2.3 and updated the template to use cms_js_tags templatetag

register = Library()

@register.filter
def bool(value):
    if value:
        return 'true'
    else:
        return 'false'