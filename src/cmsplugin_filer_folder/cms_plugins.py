from os.path import join
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from django.forms.models import ModelForm
import models
from django.conf import settings
from django.forms.widgets import Media


class FilerFolderPlugin(CMSPluginBase):
    model = models.FilerFolder
    name = _("Folder")
    render_template = "cmsplugin_filer_folder/folder.html"
    text_enabled = True
    #form = FilerFolderAdminForm
    
    def get_folder_files(self, folder, user):
        qs_files = folder.files.filter(image__isnull=True)
        if user.is_staff:
            return qs_files
        else:
            return qs_files.filter(is_public=True)
    
    def get_folder_images(self, folder, user):
        qs_files = folder.files.filter(image__isnull=False)
        if user.is_staff:
            return qs_files
        else:
            return qs_files.filter(is_public=True)
    
    def get_children(self, folder):
        return folder.get_children()
        
    def get_plugin_media(self, request, context, plugin):
        return Media(
            js=[join(settings.CMS_MEDIA_URL, path) for path in(
                'filer/slideshow2/js/mootools.js',
                'filer/slideshow2/js/slideshow.flash.js',
                'filer/slideshow2/js/slideshow.fold.js',
                'filer/slideshow2/js/slideshow.js',
                'filer/slideshow2/js/slideshow.kenburns.js',
                'filer/slideshow2/js/slideshow.push.js',
            )],
            css={
                'all': [join(settings.CMS_MEDIA_URL, path) for path in(
                    'filer/slideshow2/css/slideshow.css',)]
            }
        )
    
    def render(self, context, instance, placeholder):
        
        folder_files = self.get_folder_files(instance.folder,
                                             context['request'].user)
        folder_images = self.get_folder_images(instance.folder,
                                               context['request'].user)
        folder_folders = self.get_children(instance.folder)
        
        context.update({
            'object':instance,
            'folder_files': folder_files,
            'folder_images': folder_images,
            'folder_folders': folder_folders,
            'placeholder':placeholder
        })    
        return context
    


plugin_pool.register_plugin(FilerFolderPlugin)