from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.templatetags.static import static
from django.utils.translation import ugettext as _

from .models import FilerLinkPlugin


class FilerLinkPlugin(CMSPluginBase):
    module = 'Filer'
    model = FilerLinkPlugin
    name = _("Link")
    text_enabled = True
    raw_id_fields = ('page_link', )
    render_template = "cmsplugin_filer_link/link.html"

    def render(self, context, instance, placeholder):
        if instance.file:
            link = instance.file.url
        elif instance.mailto:
            link = "mailto:%s" % _(instance.mailto)
        elif instance.url:
            link = _(instance.url)
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
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


plugin_pool.register_plugin(FilerLinkPlugin)
