# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import NoReverseMatch
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
    name = _("Link")
    raw_id_fields = ('page_link', )
    render_template = "cmsplugin_filer_link/link.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': [
                'name',
                'url',
                'page_link',
                'mailto',
                'file',
                'link_style',
                'new_window',
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
        if instance.file:
            link = instance.file.url
        elif instance.mailto:
            link = "mailto:%s" % _(instance.mailto)
        elif instance.url:
            link = _(instance.url)
        elif instance.page_link:
            try:
                link = instance.page_link.get_absolute_url()
            except NoReverseMatch:
                link = '/'
        else:
            link = ""
        context.update({
            'link': link,
            'style': instance.link_style,
            'name': instance.name,
            'new_window': instance.new_window,
        })
        return context

    def icon_src(self, instance):
        return static("cms/img/icons/plugins/link.png")


plugin_pool.register_plugin(FilerLink2Plugin)
