from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from filer_cmsplugins.models import FilerImage, FilerTeaser, FilerFile
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class FilerImagePlugin(CMSPluginBase):
    model = FilerImage
    name = _("Image (Filer)")
    render_template = "filer_cmsplugins/image.html"
    text_enabled = True
    raw_id_fields = ('image',)
    
    def render(self, context, instance, placeholder):
        # this code for automatic 960 grid image resizing should not be here
        if instance.use_autoscale:
            try:
                theme = context['theme']
                width = int(theme.split('_')[0]) * 60
                if width < 960:
                    width -= 20
            except (KeyError, IndexError):
                width = instance.image.width
        else:
            if instance.width:
                width = instance.width
            else:
                width = instance.image.width
        if instance.height:
            height = instance.height
        else:
            height = '1000'
        
        context.update({
            'object':instance,
            'link':instance.link, 
            #'image_url':instance.scaled_image_url,
            'image_size': u'%sx%s' % (width, height),
            'placeholder':placeholder
        })
        return context
    def icon_src(self, instance):
        return instance.image.thumbnails['admin_tiny_icon']
plugin_pool.register_plugin(FilerImagePlugin)

class FilerTeaserPlugin(CMSPluginBase):
    model = FilerTeaser
    name = _("Teaser (Filer)")
    render_template = "filer_cmsplugins/teaser.html"
    
    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'object':instance, 
            'placeholder':placeholder,
            'link':link
        })
        return context
plugin_pool.register_plugin(FilerTeaserPlugin)

class FilerFilePlugin(CMSPluginBase):
    model = FilerFile
    name = _("File (Filer)")
    render_template = "filer_cmsplugins/file.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):  
        context.update({
            'object':instance, 
            'placeholder':placeholder
        })    
        return context

    def icon_src(self, instance):
        file_icon = instance.get_icon_url()
        if file_icon: return file_icon
        return settings.CMS_MEDIA_URL + u"images/plugins/file.png"
    
plugin_pool.register_plugin(FilerFilePlugin)





'''
class ImageFolderPlugin(CMSPluginBase):
    model = FolderPublication
    name = _("Image Folder from Filer")
    render_template = "image_filer/folder.html"
    text_enabled = True
    #change_form_template = 'admin/image_filer/cms/image_plugin/change_form.html'
    raw_id_fields = ('folder',)
    
    def render(self, context, instance, placeholder):
        context.dicts.append({'image_folder_publication':instance, 'placeholder':placeholder})
        return context
    def icon_src(self, instance):
        return "(none)"
plugin_pool.register_plugin(ImageFolderPlugin)

class FolderSlideshowPlugin(ImageFolderPlugin):
    name = _("Slideshow of image folder")
    class Meta:
        proxy = True
    render_template = "image_filer/slideshow2.html"
plugin_pool.register_plugin(FolderSlideshowPlugin)

'''