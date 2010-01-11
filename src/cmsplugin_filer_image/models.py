from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page
from sorl.thumbnail.main import DjangoThumbnail
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
    image = FilerImageField()
    alt_text = models.CharField(null=True, blank=True, max_length=255)
    caption = models.CharField(null=True, blank=True, max_length=255)
    
    use_autoscale = models.BooleanField(_("use automatic scaling"), default=True, 
                                        help_text=_('tries to auto scale the image based on the placeholder context'))
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    float = models.CharField(_("side"), max_length=10, blank=True, null=True, choices=FLOAT_CHOICES)
    
    free_link = models.CharField(_("link"), max_length=255, blank=True, null=True, 
                                 help_text=_("if present image will be clickable"))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True, blank=True, 
                                  help_text=_("if present image will be clickable"))
    description = models.TextField(_("description"), blank=True, null=True)
    
    '''
    @property
    def scaled_image_url(self):
        h = self.height or self.image.width
        w = self.width or self.image.height
        tn = unicode(DjangoThumbnail(self.image.file, (w,h), opts=['crop','upscale'] ))
        return tn
    '''
    def __unicode__(self):
        if self.image:
            return self.image.label
        else:
            return u"Image Publication %s" % self.caption
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
