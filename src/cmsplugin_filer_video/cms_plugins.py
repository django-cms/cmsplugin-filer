from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filer_video import settings
from cmsplugin_filer_video.models import FilerVideo
from cmsplugin_filer_video.forms import VideoForm

class FilerVideoPlugin(CMSPluginBase):
    model = FilerVideo
    name = _("Video")
    form = VideoForm
    
    render_template = "cms/plugins/video.html"
    
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
        js = ('http://ajax.googleapis.com/ajax/libs/swfobject/2.1/swfobject.js',)
        
    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder':placeholder,
        })
        return context
    
plugin_pool.register_plugin(FilerVideoPlugin)