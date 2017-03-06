# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import activate

from link2.cmsplugin_filer_link2.models import LinkHealthState


class LinkStateAdmin(admin.ModelAdmin):
    list_display = ('link', 'link_to', 'state', 'on_page', 'detected')
    list_filter = ('state',)

    def has_add_permission(self, request):
        return False

    def on_page(self, obj):
        activate(obj.link.language)
        return mark_safe('<a href="{link}" >{link}</a>'.format(link=obj.link.page.get_absolute_url()))

    def link_to(self, obj):
        if obj.state != LinkHealthState.BAD_CONFIGURED:
            activate(obj.link.language)
            return mark_safe('<a href="{link}" >{link}</a>'.format(link=obj.link.get_link()))


admin.site.register(LinkHealthState, LinkStateAdmin)
