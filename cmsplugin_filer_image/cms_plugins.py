# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.loader import select_template
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import FilerImageForm
from .models import FilerImage
from .conf import settings


class FilerImagePlugin(CMSPluginBase):
    admin_preview = False
    form = FilerImageForm
    model = FilerImage
    module = 'Filer'
    name = _("Image")
    raw_id_fields = ('image', 'page_link')
    text_enabled = True

    TEMPLATE_NAME = 'cmsplugin_filer_image/plugins/image/%s.html'
    render_template = TEMPLATE_NAME % 'default'

    fieldsets = (
        (None, {
            'fields': [
                'caption_text',
                'image',
                'image_url',
                'alt_text',
            ]
        }),
        (_('Image resizing options'), {
            'fields': (
                'use_original_image',
                ('width', 'height',),
                ('crop', 'upscale',),
                'thumbnail_option',
                'use_autoscale',
            )
        }),
        (None, {
            'fields': ('alignment',)
        }),
        (_('More'), {
            'classes': ('collapse',),
            'fields': (
                'free_link',
                'page_link',
                'file_link',
                ('original_link', 'target_blank',),
                'link_attributes',
                'description',
            ),
        }),
    )
    if settings.CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES:
        fieldsets[0][1]['fields'].append('style')

    def _get_thumbnail_options(self, context, instance):
        """
        Return the size and options of the thumbnail that should be inserted
        """
        width, height = None, None
        crop, upscale = False, False
        subject_location = False
        placeholder_width = context.get('width', None)
        placeholder_height = context.get('height', None)
        if instance.thumbnail_option:
            # thumbnail option overrides everything else
            if instance.thumbnail_option.width:
                width = instance.thumbnail_option.width
            if instance.thumbnail_option.height:
                height = instance.thumbnail_option.height
            crop = instance.thumbnail_option.crop
            upscale = instance.thumbnail_option.upscale
        else:
            if instance.use_autoscale and placeholder_width:
                # use the placeholder width as a hint for sizing
                width = int(placeholder_width)
            elif instance.width:
                width = instance.width
            if instance.use_autoscale and placeholder_height:
                height = int(placeholder_height)
            elif instance.height:
                height = instance.height
            crop = instance.crop
            upscale = instance.upscale
        if instance.image:
            if instance.image.subject_location:
                subject_location = instance.image.subject_location
            if not height and width:
                # height was not externally defined: use ratio to scale it by the width
                height = int(float(width) * float(instance.image.height) / float(instance.image.width))
            if not width and height:
                # width was not externally defined: use ratio to scale it by the height
                width = int(float(height) * float(instance.image.width) / float(instance.image.height))
            if not width:
                # width is still not defined. fallback the actual image width
                width = instance.image.width
            if not height:
                # height is still not defined. fallback the actual image height
                height = instance.image.height
        return {'size': (width, height),
                'crop': crop,
                'upscale': upscale,
                'subject_location': subject_location}

    def get_thumbnail(self, context, instance):
        if instance.image:
            return instance.image.file.get_thumbnail(self._get_thumbnail_options(context, instance))

    def render(self, context, instance, placeholder):
        options = self._get_thumbnail_options(context, instance)
        context.update({
            'instance': instance,
            'link': instance.link,
            'opts': options,
            'size': options.get('size', None),
            'placeholder': placeholder
        })
        return context

    def get_render_template(self, context, instance, placeholder):
        template = select_template((
            'cmsplugin_filer_image/plugins/image.html',  # backwards compatibility. deprecated!
            self.TEMPLATE_NAME % instance.style,
            self.TEMPLATE_NAME % 'default',
        ))
        return template

    def icon_src(self, instance):
        if instance.image:
            if getattr(settings, 'FILER_IMAGE_USE_ICON', False) and '32' in instance.image.icons:
                return instance.image.icons['32']
            else:
                # Fake the context with a reasonable width value because it is not
                # available at this stage
                thumbnail = self.get_thumbnail({'width': 200}, instance)
                return thumbnail.url
        else:
            return static("filer/icons/missingfile_%sx%s.png" % (32, 32,))
plugin_pool.register_plugin(FilerImagePlugin)
