from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.models import CMSPlugin, Page
from cms.models.fields import PageField
from filer.fields.file import FilerFileField

DEFULT_LINK_STYLES = (
    (" ", "Default"),
)

LINK_STYLES = getattr(settings, "FILER_LINK_STYLES", DEFULT_LINK_STYLES)

class FilerLinkPlugin(CMSPlugin):
    name = models.CharField(_('name'), max_length=255)
    url = models.CharField(_("url"), blank=True, null=True, max_length=255)
    page_link = PageField(verbose_name=_("page"), blank=True, null=True,
             help_text=_("A link to a page has priority over urls."))
    mailto = models.EmailField(_("mailto"), blank=True, null=True,
             help_text=_("An email address has priority over both pages and urls"))
    link_style = models.CharField(_("link style"), max_length=255,
                choices=LINK_STYLES, default=" ")
    new_window = models.BooleanField(_("new window?"), default=False,
                help_text=_("Do you want this link to open a new window?"))
    file = FilerFileField(blank=True, null=True)


    def __unicode__(self):
        return u'%s' % self.name

