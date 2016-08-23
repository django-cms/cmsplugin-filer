from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _
from . import models
from .conf import settings

from filer.models.filemodels import File
from filer.models.foldermodels import Folder
from filer.models.abstract import BaseImage


class FilerFolderPlugin(CMSPluginBase):
    module = 'Filer'
    model = models.FilerFolder
    name = _("Folder")
    TEMPLATE_NAME = 'cmsplugin_filer_folder/plugins/folder/%s.html'
    render_template = TEMPLATE_NAME % 'default'
    text_enabled = False
    admin_preview = False

    fieldsets = (
        (None, {'fields': ['title', 'folder']}),
    )
    if settings.CMSPLUGIN_FILER_FOLDER_STYLE_CHOICES:
        fieldsets[0][1]['fields'].append('style')

    def get_folder_files(self, folder, user):
        qs_files = folder.files.not_instance_of(BaseImage)
        if user.is_staff:
            return qs_files
        else:
            return qs_files.filter(is_public=True)

    def get_folder_images(self, folder, user):
        qs_files = folder.files.instance_of(BaseImage)
        if user.is_staff:
            return qs_files
        else:
            return qs_files.filter(is_public=True)

    def get_children(self, folder):
        return folder.get_children()

    def render(self, context, instance, placeholder):
        user = context['request'].user

        if instance.folder_id:
            folder_files = self.get_folder_files(instance.folder, user)
            folder_images = self.get_folder_images(instance.folder, user)
            folder_folders = self.get_children(instance.folder)
        else:
            folder_files = File.objects.none()
            folder_images = BaseImage.objects.none()
            folder_folders = Folder.objects.none()

        context.update({
            'object': instance,
            'folder_files': sorted(folder_files),
            'folder_images': sorted(folder_images),
            'folder_folders': folder_folders,
            'placeholder': placeholder
        })
        return context

    def get_render_template(self, context, instance, placeholder):
        template = select_template((
            'cmsplugin_filer_folder/folder.html',  # backwards compatibility. deprecated!
            self.TEMPLATE_NAME % instance.style,
            self.TEMPLATE_NAME % 'default',
        ))
        return template


plugin_pool.register_plugin(FilerFolderPlugin)
