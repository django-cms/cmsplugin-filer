# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.models import CMSPlugin
from cms.models.fields import PageField

from filer.fields.file import FilerFileField
from filer.utils.compatibility import python_2_unicode_compatible

from djangocms_attributes_field.fields import AttributesField


DEFULT_LINK_STYLES = (
    (" ", "Default"),
)

LINK_STYLES = getattr(settings, "FILER_LINK_STYLES", DEFULT_LINK_STYLES)

EXCLUDED_KEYS = ['class', 'href', 'target', ]


@python_2_unicode_compatible
class FilerLinkPlugin(CMSPlugin):
    name = models.CharField(_('name'), max_length=255)
    url = models.CharField(_("url"), blank=True, null=True, max_length=2000)
    page_link = PageField(
        verbose_name=_("page"),
        blank=True,
        null=True,
        help_text=_("A link to a page has priority over urls."),
        on_delete=models.SET_NULL,
    )
    mailto = models.EmailField(_("mailto"), blank=True, null=True, max_length=254,
             help_text=_("An email address has priority over both pages and urls"))
    link_style = models.CharField(_("link style"), max_length=255,
                choices=LINK_STYLES, default=LINK_STYLES[0][0])
    new_window = models.BooleanField(_("new window?"), default=False,
                help_text=_("Do you want this link to open a new window?"))
    file = FilerFileField(blank=True, null=True, on_delete=models.SET_NULL)
    link_attributes = AttributesField(excluded_keys=EXCLUDED_KEYS, blank=True,
                                      help_text=_('Optional. Adds HTML attributes to the rendered link.'))
    cmsplugin_ptr = models.OneToOneField(
        to=CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return self.name
