
import os
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
import models
from django.conf import settings
from django.template import Context, Template
import warnings
from django import forms
from django.core.exceptions import ValidationError

from filer.settings import FILER_STATICMEDIA_PREFIX


class FilerImagePluginForm(forms.ModelForm):
    class Meta:
        model = models.FilerImage

    def clean_link_options(self):
        link_options = self.cleaned_data['link_options']
        if (link_options == 2 and
            not self.cleaned_data.get('free_link', '')):
            raise ValidationError('Link filed is required!')
        elif (link_options == 3 and
              not self.cleaned_data.get('page_link', None)):
            raise ValidationError('Page link is required!')
        elif (link_options == 4 and
              not self.cleaned_data.get('file_link', None)):
            raise ValidationError('File link is required!')
        elif (link_options == 5 and
              not self.cleaned_data.get('image', None)):
            raise ValidationError('Image field is required!')
        return self.cleaned_data['link_options']


class FilerImagePlugin(CMSPluginBase):
    form = FilerImagePluginForm
    module = 'Filer'
    model = models.FilerImage
    name = _("Image")
    render_template = "cmsplugin_filer_image/image.html"
    text_enabled = True
    raw_id_fields = ('image',)
    admin_preview = False
    fieldsets = (
        (None, {
            'fields': (('alt_text', 'show_alt'),
                       ('caption_text', 'show_caption'),
                       ('credit_text', 'show_credit'),
                       ('image', ), )
        }),
        (_('Image options'), {
            'fields': ('thumbnail_option',
                       'alignment',
                       'link_options',
                       ('free_link', 'target_blank',),
                       'page_link',
                       'file_link',)
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': (
                ('width', 'height', 'crop', 'maintain_aspect_ratio'),
                ('vertical_space', 'horizontal_space',),
                'border',
            )
        }),
    )

    class Media:
        js = ("admin/js/popup_handling_override.js",
              "admin/js/link_options.js",
              "admin/js/advanced_panel_text_additions.js")

    def _get_thumbnail_options(self, context, instance):
        """
        Return the size and options of the thumbnail that should be inserted
        """
        width, height = None, None
        crop, upscale = False, False
        subject_location = False
        placeholder_width = context.get('width', None)
        placeholder_height = context.get('height', None)
        if instance.width or instance.height:
            # width and height options override everything else
            if instance.width:
                width = instance.width
            if instance.height:
                height = instance.height
            crop = instance.crop
            upscale = instance.upscale
        elif instance.thumbnail_option:
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
            if instance.use_autoscale and placeholder_height:
                height = int(placeholder_height)

        if instance.image:
            if instance.image.subject_location:
                subject_location = instance.image.subject_location
            if not height and width:
                # height was not externally defined: use ratio to scale it by the width
                height = int( float(width)*float(instance.image.height)/float(instance.image.width) )
            if not width and height:
                # width was not externally defined: use ratio to scale it by the height
                width = int( float(height)*float(instance.image.width)/float(instance.image.height) )
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
            return instance.image.image.file.get_thumbnail(self._get_thumbnail_options(context, instance))

    def render(self, context, instance, placeholder):
        options = self._get_thumbnail_options(context, instance)
        #Styles for images can be set from 2 places:
        #         1. filer image popup
        #         2. right click on the img from text plg and select Alignment option
        # The style set at point 1. can be accessed with instance.style
        # The style set at point 2. can be accessed with context["inherited_from_parent"]["style"]
        # As you can see below, the style set at point 1. have priority
        # The style set at point 2. is taken into account to keep the consistence with all other plugins.
        style = instance.style or context.get("inherited_from_parent", {}).get("style", "")
        context.update({
            'instance': instance,
            'style': style,
            'link': instance.link,
            'opts': options,
            'size': options.get('size',None),
            'placeholder': placeholder
        })
        return context

    def icon_src(self, instance):
        if instance.image:
            if getattr(settings, 'FILER_IMAGE_USE_ICON', False) and '32' in instance.image.icons:
                return instance.image.icons['32']
            else:
                # Fake the context with a reasonable width value because it is not
                # available at this stage
                thumbnail = self.get_thumbnail({'width':200}, instance)
                return thumbnail.url
        else:
            return os.path.normpath(u"%s/icons/missingfile_%sx%s.png" % (FILER_STATICMEDIA_PREFIX, 32, 32,))


plugin_pool.register_plugin(FilerImagePlugin)
