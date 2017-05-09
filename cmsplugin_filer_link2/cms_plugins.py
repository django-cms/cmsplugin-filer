# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.templatetags.static import static
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import FilerLink2Form
from .models import FilerLink2Plugin as FilerLinkPluginModel


class FilerLink2Plugin(CMSPluginBase):
    form = FilerLink2Form
    model = FilerLinkPluginModel
    module = 'Filer'
    name = _('Link')
    raw_id_fields = ('page_link', )
    render_template = "cmsplugin_filer_link/link.html"
    change_form_template = 'cmsplugin_filer_link/change_form.html'
    text_enabled = True
    fieldsets = (
        (None, {
            'fields': [
                'name',
            ]
        }),
        (None, {
            'classes': ['link2-destination', ],
            'fields': [
                'url',
                'page_link',
                'mailto',
                'file',
            ],
        }),
        (None, {
            'fields': [
                'new_window',
                'link_style',
            ]
        }),
        (_('Advanced'), {
            'classes': ['collapse', ],
            'fields': [
                'link_attributes',
            ]
        })
    )

    def render(self, context, instance, placeholder):
        context = super(FilerLink2Plugin, self).render(context, instance, placeholder)
        link = instance.get_link()
        context.update({
            'link': link,
            'style': instance.link_style,
            'name': instance.name,
            'new_window': instance.new_window,
        })
        try:
            # check if we are in edit mode, so we show link health
            if context['request'].toolbar.edit_mode:
                state = instance.get_linkstate()
                if state:
                    context.update({
                        'link_state': state,
                    })
        except (KeyError, AttributeError):
            pass
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        # The active destination determines which destination tab should be set to active. If the field is not set
        # yet, we make the first tab (url) active
        context.update({
            'active_destination': 'url' if add is True or obj.active_destination is None else obj.active_destination
        })
        return super(FilerLink2Plugin, self).render_change_form(request, context, add, change, form_url, obj)

    def icon_src(self, instance):
        return static("cms/img/icons/plugins/link.png")


plugin_pool.register_plugin(FilerLink2Plugin)
