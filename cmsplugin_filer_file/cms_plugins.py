# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.loader import select_template
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .conf import settings
from .forms import FilerFileForm
from .models import FilerFile


class FilerFilePlugin(CMSPluginBase):
    form = FilerFileForm
    module = 'Filer'
    model = FilerFile
    name = _("File")
    TEMPLATE_NAME = 'cmsplugin_filer_file/plugins/file/%s.html'
    render_template = TEMPLATE_NAME % 'default'
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': [
                'title', 'file', 'target_blank'
            ]
        }),
        (_('Advanced'), {
            'classes': ['collapse', ],
            'fields': [
                'link_attributes',
            ]
        })
    )

    if settings.CMSPLUGIN_FILER_FILE_STYLE_CHOICES:
        fieldsets[0][1]['fields'].append('style')

    def render(self, context, instance, placeholder):
        context['object'] = instance
        return super(FilerFilePlugin, self).render(context, instance, placeholder)

    def get_render_template(self, context, instance, placeholder):
        template = select_template((
            'cmsplugin_filer_file/plugins/file.html',  # backwards compatibility. deprecated!
            self.TEMPLATE_NAME % instance.style,
            self.TEMPLATE_NAME % 'default',
        ))
        return template

    def icon_src(self, instance):
        file_icon = instance.get_icon_url()

        if file_icon:
            return file_icon
        return static("filer/icons/file_%sx%s.png" % (32, 32,))

plugin_pool.register_plugin(FilerFilePlugin)
