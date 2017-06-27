# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import activate
from django.utils.translation import ugettext as _

from .models import LinkHealthState


class LinkStateAdmin(admin.ModelAdmin):
    list_display = ('link_name', 'link_to', 'state', 'on_page', 'detected')
    list_filter = ('state',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def link_name(self, obj):
        return obj.link
    link_name.allow_tags = True
    link_name.short_description = _('Link name')

    def on_page(self, obj):
        activate(obj.link.language)
        return mark_safe('<a href="{link}" >{link}</a>'.format(link=obj.link.page.get_absolute_url()))
    on_page.allow_tags = True
    on_page.short_description = _('On page')

    def link_to(self, obj):
        if obj.state != LinkHealthState.BAD_CONFIGURED:
            activate(obj.link.language)
            return mark_safe('<a href="{link}" >{link}</a>'.format(link=obj.link.get_link()))
    link_to.allow_tags = True
    link_to.short_description = _('Links to')


admin.site.register(LinkHealthState, LinkStateAdmin)
