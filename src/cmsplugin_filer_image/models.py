from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page
from cms.models.fields import PageField
from django.utils.translation import ugettext_lazy as _
from posixpath import join, basename, splitext, exists
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from cms import settings as cms_settings
from django.conf import settings

class FilerImage(CMSPlugin):
    LEFT = "left"
    RIGHT = "right"
    FLOAT_CHOICES = ((LEFT, _("left")),
                     (RIGHT, _("right")),
                     )
    caption = models.CharField(_("caption"), null=True, blank=True, max_length=255)
    image = FilerImageField(null=True, blank=True, default=None)
    image_url = models.URLField(_("alternative image url"), verify_exists=False, null=True, blank=True, default=None)
    alt_text = models.CharField(_("alt text"), null=True, blank=True, max_length=255)
    thumbnail_option = models.ForeignKey('ThumbnailOption', null=True, blank=True, verbose_name=_("thumbnail option"))
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
                          help_text=_("if present image will be clickable"))
    description = models.TextField(_("description"), blank=True, null=True)
    
    class Meta:
        verbose_name = _("filer image")
        verbose_name_plural = _("filer images")
    
    def clean(self):
        from django.core.exceptions import ValidationError
        # Make sure that either image or image_url is set
        if (not self.image and not self.image_url) or (self.image and self.image_url):
            raise ValidationError(_('Either an image or an image url must be selected.'))

    
    def __unicode__(self):
        if self.image:
            return self.image.label
        else:
            return unicode( _("Image Publication %(caption)s") % self.caption)
        return ''
    @property
    def alt(self): 
        return self.alt_text
    @property
    def link(self):
        if self.free_link:
            return self.free_link
        elif self.page_link and self.page_link:
            return self.page_link.get_absolute_url()
        else:
            return ''
        
        
class ThumbnailOption(models.Model):
    """
    This class defines the option use to create the thumbnail.
    """
    name = models.CharField(max_length=100)
    width = models.IntegerField(help_text=_('width in pixel.'))
    height = models.IntegerField(help_text=_('height in pixel.'))
    crop = models.BooleanField(default=True)
    upscale = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('width', 'height')
        
    def __unicode__(self):
        return u'%s -- %s x %s' %(self.name, self.width, self.height)
        

    