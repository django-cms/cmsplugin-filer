from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

import models


class FilerFilePlugin(CMSPluginBase):
    module = 'Filer'
    model = models.FilerFile
    name = _("File")
    render_template = "cmsplugin_filer_file/file.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FilerFilePlugin)
