# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from filer.fields.file import FilerFileField
from filer.utils.compatibility import python_2_unicode_compatible

from cmsplugin_filer_utils import FilerPluginManager
from djangocms_attributes_field.fields import AttributesField

from .conf import settings


@python_2_unicode_compatible
class FilerFile(CMSPlugin):
    """
    Plugin for storing any type of file.

    Default template displays download link with icon (if available) and file size.

    This could be updated to use the mimetypes library to determine the type of file rather than
    storing a separate icon for each different extension.

    The icon search is currently performed within get_icon_url; this is probably a performance concern.
    """
    STYLE_CHOICES = settings.CMSPLUGIN_FILER_FILE_STYLE_CHOICES
    DEFAULT_STYLE = settings.CMSPLUGIN_FILER_FILE_DEFAULT_STYLE
    EXCLUDED_KEYS = ['href', 'target', ]

    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    file = FilerFileField(
        verbose_name=_('file'),
        null=True,
        on_delete=models.SET_NULL,
    )
    target_blank = models.BooleanField(_('Open link in new window'), default=False)
    style = models.CharField(
        _('Style'), choices=STYLE_CHOICES, default=DEFAULT_STYLE, max_length=255, blank=True)
    link_attributes = AttributesField(excluded_keys=EXCLUDED_KEYS, blank=True,
                                      help_text=_('Optional. Adds HTML attributes to the rendered link.'))
    cmsplugin_ptr = models.OneToOneField(
        to=CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    objects = FilerPluginManager(select_related=('file',))

    def get_icon_url(self):
        if self.file_id:
            return self.file.icons['32']
        return ''

    def file_exists(self):
        if self.file_id:
            return self.file.file.storage.exists(self.file.file.name)
        return False

    def get_file_name(self):
        if not self.file_id:
            return ''

        if self.file.name in ('', None):
            name = "%s" % (self.file.original_filename,)
        else:
            name = "%s" % (self.file.name,)
        return name

    def get_ext(self):
        return self.file.extension

    def __str__(self):
        if self.title:
            return self.title
        elif self.file_id:
            # added if, because it raised attribute error when file wasnt defined
            return self.get_file_name()
        return "<empty>"

    search_fields = ('title',)
