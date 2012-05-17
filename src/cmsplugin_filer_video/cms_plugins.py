import os
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filer_video import settings
from cmsplugin_filer_video.models import FilerVideo
from cmsplugin_filer_video.forms import VideoForm
from filer.settings import FILER_STATICMEDIA_PREFIX

class FilerVideoPlugin(CMSPluginBase):
    module = 'Filer'
    model = FilerVideo
    name = _("Video")
    form = VideoForm

    render_template = "cmsplugin_filer_video/video.html"
    text_enabled = True

    general_fields = [
        ('movie', 'movie_url'),
        'image',
        ('width', 'height'),
        'auto_play',
        'auto_hide',
        'fullscreen',
        'loop',
    ]
    color_fields = [
        'bgcolor',
        'textcolor',
        'seekbarcolor',
        'seekbarbgcolor',
        'loadingbarcolor',
        'buttonoutcolor',
        'buttonovercolor',
        'buttonhighlightcolor',
    ]

    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
    ]
    if settings.VIDEO_PLUGIN_ENABLE_ADVANCED_SETTINGS:
        fieldsets += [
            (_('Color Settings'), {
                'fields': color_fields,
                'classes': ('collapse',),
            }),
        ]

    class PluginMedia:
        js = ('https://ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js',)

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder':placeholder,
        })
        return context

    def icon_src(self, instance):
        return os.path.normpath(u"%s/icons/video_%sx%s.png" % (FILER_STATICMEDIA_PREFIX, 32, 32,))
plugin_pool.register_plugin(FilerVideoPlugin)
