# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin
from django.core.files.uploadedfile import SimpleUploadedFile


def create_image_plugin(filename, image, parent_plugin, **kwargs):
    """
    Used for drag-n-drop image insertion with djangocms-text-ckeditor.
    Set TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin' to enable.
    """
    from cmsplugin_filer_image.models import FilerImage
    from filer.models import Image
    image_plugin = FilerImage()
    image_plugin.placeholder = parent_plugin.placeholder
    image_plugin.parent = CMSPlugin.objects.get(pk=parent_plugin.id)
    image_plugin.position = CMSPlugin.objects.filter(parent=parent_plugin).count()
    image_plugin.language = parent_plugin.language
    image_plugin.plugin_type = 'FilerImagePlugin'
    image.seek(0)
    image_model = Image.objects.create(file=SimpleUploadedFile(name=filename, content=image.read()))
    image_plugin.image = image_model
    image_plugin.save()
    return image_plugin


def update_image_plugin(plugin, width=None, height=None):
    plugin.width = width
    plugin.heigt = height
    plugin.save()
