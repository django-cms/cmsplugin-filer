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

class FilerTeaser(CMSPlugin):
    """
    A Teaser
    """
    title = models.CharField(_("title"), max_length=255)
    image = FilerImageField(blank=True, null=True)
    
    use_autoscale = models.BooleanField(_("use automatic scaling"), default=True, 
                                        help_text=_('tries to auto scale the image based on the placeholder context'))
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    
    free_link = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True, blank=True, help_text=_("if present image will be clickable"))
    description = models.TextField(_("description"), blank=True, null=True)
    
    def __unicode__(self):
        return self.title
