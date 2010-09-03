from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
import models
from django.conf import settings

class FilerFolderPlugin(CMSPluginBase):
    model = models.FilerFolder
    name = _("Folder")
    render_template = "cmsplugin_filer_folder/folder.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):  
        context.update({
            'object':instance, 
            'placeholder':placeholder
        })    
        return context

plugin_pool.register_plugin(FilerFolderPlugin)