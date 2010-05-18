from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
import models
from django.conf import settings

class FilerTeaserPlugin(CMSPluginBase):
    model = models.FilerTeaser
    name = _("Teaser (Filer)")
    render_template = "cmsplugin_filer_teaser/teaser.html"
    
    def render(self, context, instance, placeholder):
        if instance.image:
            # TODO: this scaling code needs to be in a common place
            placeholder_width = context.get('width', None)
            if instance.use_autoscale and placeholder_width:
                width = placeholder_width
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
            context.update({'image_size': u'%sx%s' % (width, height),
                            'image_width': width,
                            'image_height': height})
        context.update({
            'object':instance, 
            'placeholder':placeholder,
            'link':instance.link,
        })
        return context
plugin_pool.register_plugin(FilerTeaserPlugin)
