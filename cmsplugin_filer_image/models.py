from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.utils.compatibility import python_2_unicode_compatible
from cmsplugin_filer_utils import FilerPluginManager
from .conf import settings


@python_2_unicode_compatible
class FilerImage(CMSPlugin):
    LEFT = "left"
    RIGHT = "right"
    FLOAT_CHOICES = ((LEFT, _("left")),
                     (RIGHT, _("right")),
                     )
    STYLE_CHOICES = settings.CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES
    DEFAULT_STYLE = settings.CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE
    style = models.CharField(
        _('Style'), choices=STYLE_CHOICES, default=DEFAULT_STYLE, max_length=50, blank=True)
    caption_text = models.CharField(_("caption text"), null=True, blank=True, max_length=255)
    image = FilerImageField(null=True, blank=True, default=None, verbose_name=_("image"))
    image_url = models.URLField(_("alternative image url"), null=True, blank=True, default=None)
    alt_text = models.CharField(_("alt text"), null=True, blank=True, max_length=255)
    use_original_image = models.BooleanField(_("use the original image"), default=False,
        help_text=_('do not resize the image. use the original image instead.'))
    thumbnail_option = models.ForeignKey('ThumbnailOption', null=True, blank=True, verbose_name=_("thumbnail option"),
                                        help_text=_('overrides width, height, crop and upscale with values from the selected thumbnail option'))
    use_autoscale = models.BooleanField(_("use automatic scaling"), default=False,
                                        help_text=_('tries to auto scale the image based on the placeholder context'))
    width = models.PositiveIntegerField(_("width"), null=True, blank=True)
    height = models.PositiveIntegerField(_("height"), null=True, blank=True)
    crop = models.BooleanField(_("crop"), default=True)
    upscale = models.BooleanField(_("upscale"), default=True)
    alignment = models.CharField(_("image alignment"), max_length=10, blank=True, null=True, choices=FLOAT_CHOICES)

    free_link = models.CharField(_("link"), max_length=255, blank=True, null=True,
                                 help_text=_("if present image will be clickable"))
    page_link = PageField(null=True, blank=True,
                          help_text=_("if present image will be clickable"),
                          verbose_name=_("page link"))
    file_link = FilerFileField(null=True, blank=True, default=None, verbose_name=_("file link"), help_text=_("if present image will be clickable"), related_name='+')
    original_link = models.BooleanField(_("link original image"), default=False, help_text=_("if present image will be clickable"))
    description = models.TextField(_("description"), blank=True, null=True)
    target_blank = models.BooleanField(_('Open link in new window'), default=False)

    # we only add the image to select_related. page_link and file_link are FKs
    # as well, but they are not used often enough to warrant the impact of two
    # additional LEFT OUTER JOINs.
    objects = FilerPluginManager(select_related=('image',))


    class Meta:
        verbose_name = _("filer image")
        verbose_name_plural = _("filer images")

    def clean(self):
        from django.core.exceptions import ValidationError
        # Make sure that either image or image_url is set
        if (not self.image and not self.image_url) or (self.image and self.image_url):
            raise ValidationError(_('Either an image or an image url must be selected.'))


    def __str__(self):
        if self.image:
            return self.image.label
        else:
            return _("Image Publication %(caption)s") % {'caption': self.caption or self.alt}
        return ''
    @property
    def caption(self):
        if self.image:
            return self.caption_text or self.image.default_caption
        else:
            return self.caption_text
    @property
    def alt(self):
        if self.image:
            return self.alt_text or self.image.default_alt_text or self.image.label
        else:
            return self.alt_text
    @property
    def link(self):
        if self.free_link:
            return self.free_link
        elif self.page_link:
            return self.page_link.get_absolute_url()
        elif self.file_link:
            return self.file_link.url
        elif self.original_link:
            if self.image:
                return self.image.url
            else:
                return self.image_url
        else:
            return ''


@python_2_unicode_compatible
class ThumbnailOption(models.Model):
    """
    This class defines the option use to create the thumbnail.
    """
    name = models.CharField(_("name"), max_length=100)
    width = models.IntegerField(_("width"), help_text=_('width in pixel.'))
    height = models.IntegerField(_("height"), help_text=_('height in pixel.'))
    crop = models.BooleanField(_("crop"), default=True)
    upscale = models.BooleanField(_("upscale"), default=True)

    class Meta:
        ordering = ('width', 'height')
        verbose_name = _("thumbnail option")
        verbose_name_plural = _("thumbnail options")

    def __str__(self):
        return '%s -- %s x %s' % (self.name, self.width, self.height)

    @property
    def as_dict(self):
        """
        This property returns a dictionary suitable for Thumbnailer.get_thumbnail()

        Sample code:
            # thumboption_obj is a ThumbnailOption instance
            # filerimage is a Image instance
            option_dict = thumboption_obj.as_dict
            thumbnailer = filerimage.easy_thumbnails_thumbnailer
            thumb_image = thumbnailer.get_thumbnail(option_dict)
        """
        return {"size":(self.width,self.height), "width":self.width,
                "height":self.height,"crop":self.crop,"upscale":self.upscale}
