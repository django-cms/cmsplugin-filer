
import os, re
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
import models
from django.conf import settings
from django.template import Context, Template
import warnings
from django import forms
from django.core.exceptions import ValidationError
from cmsplugin_filer_image.models import ThumbnailOption
from django.db.models.query import EmptyQuerySet

from filer.settings import FILER_STATICMEDIA_PREFIX

try:
    import json
except:
    import simplejson as json


class FilerImagePluginForm(forms.ModelForm):
    class Meta:
        model = models.FilerImage

    def __init__(self, *args, **kwargs):
        super(FilerImagePluginForm, self).__init__(*args, **kwargs)

        link_options_field = self.fields.get('link_options', None)
        # the values are css classes of the formsets that are shown/hidden
        # when link_options is changed
        formset_divs_cls = {
            models.FilerImage.OPT_NO_LINK: 'None',
            models.FilerImage.OPT_ADD_LINK: '.form-row.field-free_link.field-target_blank',
            models.FilerImage.OPT_PAGE_LINK: '.form-row.field-page_link',
            models.FilerImage.OPT_FILE_LINK: '.form-row.field-file_link',
        }
        if link_options_field:
            # this attr will be used in link_options.js
            link_options_field.widget.attrs = {
                'data': json.dumps(formset_divs_cls)
            }

        qs = ThumbnailOption.objects.get_default_options(
                self.instance.has_attached_image())
        self.fields['thumbnail_option'].widget.choices.queryset = qs

        #This html is appended in the document by popup_helper_image.js.
        # I need to setup it here because STATIC_URL is not available in
        # popup_helper_image.js
        popup_html= _("<div class='helper_img'><a href='%sadmin/img/image-caption-credit.jpg'>"
                      "<img src='%sadmin/img/icon-unknown.gif' width='16' height='16'>"
                      "Wait, how are these fields displayed?</a></div>" % (
                          settings.STATIC_URL, settings.STATIC_URL))
        self.fields['image'].widget.attrs.update({'helper_popup': popup_html})

    def clean_free_link(self):
        link_options = self.cleaned_data['link_options']
        if (link_options == self.instance.OPT_ADD_LINK and
            not self.cleaned_data.get('free_link', '')):
            raise ValidationError('Link filed is required!')
        return self.cleaned_data['free_link']

    def clean_page_link(self):
        link_options = self.cleaned_data['link_options']
        if (link_options == self.instance.OPT_PAGE_LINK and
            not self.cleaned_data.get('page_link', None)):
            raise ValidationError('Page link is required!')
        return self.cleaned_data['page_link']

    def clean_file_link(self):
        link_options = self.cleaned_data['link_options']
        if (link_options == self.instance.OPT_FILE_LINK and
            not self.cleaned_data.get('file_link', None)):
            raise ValidationError('File link is required!')
        return self.cleaned_data['file_link']


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
            'fields': (('alt_text',),
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
              "admin/js/advanced_panel_text_additions.js",
              "admin/js/caption_formatting.js",
              "admin/js/popup_helper_image.js")

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
            if placeholder_width:
                # use the placeholder width as a hint for sizing
                width = int(placeholder_width)
            if placeholder_height:
                height = int(placeholder_height)

        if instance.has_attached_image():
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
        if instance.has_attached_image():
            return instance.image.image.file.get_thumbnail(self._get_thumbnail_options(context, instance))

    def _get_default_horiz_space(self, instance, context):
        if ("inherited_from_parent" in context and
            not instance.horiz_space and
            not instance.alignment == instance.CENTER):
            return instance.DEFAULT_HORIZONTAL_SPACE
        else:
            return ''

    def render(self, context, instance, placeholder):
        options = self._get_thumbnail_options(context, instance)

        #Styles for images can be set from 2 places:
        #         1. filer image popup
        #         2. right click on the img from text plg and select Alignment option
        # The style set at point 1. can be accessed with instance.style
        # The style set at point 2. can be accessed with context["inherited_from_parent"]["style"]
        # As you can see below, the style set at point 1. have priority
        # The style set at point 2. is taken into account to keep the consistence with all other plugins.
        text_plg_style = context.get("inherited_from_parent", {}).get("style", "")
        style = text_plg_style + instance.style

        context.update({
            'instance': instance,
            'style': style,
            'link': instance.link,
            'opts': options,
            'size': options.get('size', None),
            'placeholder': placeholder,
            'default_horiz_space': self._get_default_horiz_space(instance, context)
        })
        return context

    def icon_src(self, instance):
        if instance.has_attached_image():
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
