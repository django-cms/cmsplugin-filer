from __future__ import unicode_literals

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.template.loader import select_template
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _
from . import models
from .conf import settings


class FilerFilePlugin(CMSPluginBase):
    module = 'Filer'
    model = models.FilerFile
    name = _("File")
    TEMPLATE_NAME = 'cmsplugin_filer_file/plugins/file/%s.html'
    render_template = TEMPLATE_NAME % 'default'
    text_enabled = True

    fieldsets = (
        (None, {'fields': [
            'title',
            'file',
            'target_blank'
        ]}),
    )
    if settings.CMSPLUGIN_FILER_FILE_STYLE_CHOICES:
        fieldsets[0][1]['fields'].append('style')

    def render(self, context, instance, placeholder):
        self.render_template = select_template((
            'cmsplugin_filer_file/plugins/file.html',  # backwards compatibility. deprecated!
            self.TEMPLATE_NAME % instance.style,
            self.TEMPLATE_NAME % 'default')
        )
        context.update({
            'object':instance,
            'placeholder':placeholder
        })
        return context

    def icon_src(self, instance):
        file_icon = instance.get_icon_url()
        if file_icon:
            return file_icon
        return static("filer/icons/file_%sx%s.png" % (32, 32,))

plugin_pool.register_plugin(FilerFilePlugin)
