import os
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
import models
from django.conf import settings

from filer.settings import FILER_ADMIN_ICON_SIZES, FILER_PUBLICMEDIA_PREFIX, FILER_PRIVATEMEDIA_PREFIX, FILER_STATICMEDIA_PREFIX

class FilerImagePlugin(CMSPluginBase):
    model = models.FilerImage
    name = _("Image")
    render_template = "cmsplugin_filer_image/image.html"
    text_enabled = True
    raw_id_fields = ('image',)
    admin_preview = False
    fieldsets = (
        (None, {
            'fields': ('caption', 'image', 'image_url', 'alt_text',
                       'thumbnail_option',)
        }),
        ('advanced thumbnail option', {
            'classes': ('collapse',),
            'fields': ('use_autoscale', 'width', 'height', 'float')
        }),
        ('More', {
            'classes': ('collapse',),
            'fields': ('free_link', 'page_link', 'description',)
        }),        
        
    )
    
    def _get_thumbnail_size(self, context, instance):
        """
        Return the size of the thumbnail that should be inserted
        """
        
        placeholder_width = context.get('width', None)
        if instance.thumbnail_option:
            if instance.thumbnail_option.width:
                width = instance.thumbnail_option.width
            if instance.thumbnail_option.height:
                height = instance.thumbnail_option.height
            else:
                # height was not externally defined: use ratio to scale it by the width
                height = int( float(width)*float(instance.image.height)/float(instance.image.width) )
        elif instance.use_autoscale and placeholder_width:
            # use the placeholder width as a hint for sizing
            width = placeholder_width
            # height was not externally defined: use ratio to scale it by the width
            height = int( float(width)*float(instance.image.height)/float(instance.image.width) )
        else:
            if instance.width:
                width = instance.width
            else:
                width = instance.image.width
            if instance.height:
                height = instance.height
                if width == instance.image.width:
                    # width was not externally defined: use ratio to scale it by the height
                    width = int( float(height)*float(instance.image.width)/float(instance.image.height) )
            else:
                # height was not externally defined: use ratio to scale it by the width
                height = int( float(width)*float(instance.image.height)/float(instance.image.width) )
        return (width, height)
       
    def get_thumbnail(self, context, instance):
        if instance.image:
            width, height = self._get_thumbnail_size(context, instance)
            # build thumbnail options
            thumbnail_opts = {
                'size': self._get_thumbnail_size(context, instance),
                'crop': True, #instance.crop,
                'upscale': True, #instance.upscale,
            }
            return instance.image.image.file.get_thumbnail(thumbnail_opts)
    
    def render(self, context, instance, placeholder):
        if instance.image:
            width, height = self._get_thumbnail_size(context, instance)
        thumbnail = self.get_thumbnail(context, instance)
        context.update({
            'object':instance,
            'link':instance.link,
            'thumbnail': thumbnail,
            'placeholder':placeholder
        })
        return context
    
    def icon_src(self, instance):
        if instance.image:
            # TODO: Find a cleaner way
            # Fake the context because it is not available at this stage
            # this will cause a bug when using autoscale
            thumbnail = self.get_thumbnail({}, instance)
            return thumbnail.url
        else:
            return os.path.normpath(u"%s/icons/missingfile_%sx%s.png" % (FILER_STATICMEDIA_PREFIX, 32, 32,))
plugin_pool.register_plugin(FilerImagePlugin)
