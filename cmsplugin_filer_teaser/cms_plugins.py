from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from django.template.loader import select_template
from . import models
from .conf import settings


class FilerTeaserPlugin(CMSPluginBase):
    """
    TODO: this plugin is becoming very similar to the image plugin... code
          should be re-used somehow.
    """
    module = 'Filer'
    model = models.FilerTeaser
    raw_id_fields = ('page_link',)
    name = _("Teaser")
    TEMPLATE_NAME = 'cmsplugin_filer_teaser/plugins/teaser/%s.html'
    render_template = TEMPLATE_NAME % 'default'

    fieldsets = (
        (None, {'fields': [
            'title',
            'image',
            'image_url',
            'description',
        ]}),
        (_('More'), {
            'classes': ('collapse',),
            'fields': [
                'use_autoscale',
                ('width', 'height'),
                'free_link',
                'page_link',
                'target_blank'
            ]
        })
    )
    if settings.CMSPLUGIN_FILER_TEASER_STYLE_CHOICES:
        fieldsets[0][1]['fields'].append('style')

    def _get_thumbnail_options(self, context, instance):
        """
        Return the size and options of the thumbnail that should be inserted
        """
        width, height = None, None
        subject_location = False
        placeholder_width = context.get('width', None)
        placeholder_height = context.get('height', None)
        if instance.use_autoscale and placeholder_width:
            # use the placeholder width as a hint for sizing
            width = int(placeholder_width)
        if instance.use_autoscale and placeholder_height:
            height = int(placeholder_height)
        elif instance.width:
            width = instance.width
        if instance.height:
            height = instance.height
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
            'cmsplugin_filer_teaser/plugins/teaser.html',  # backwards compatibility. deprecated!
            self.TEMPLATE_NAME % instance.style,
            self.TEMPLATE_NAME % 'default',
        ))
        return template

plugin_pool.register_plugin(FilerTeaserPlugin)
