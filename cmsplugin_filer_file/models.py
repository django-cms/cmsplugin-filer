from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from filer.utils.compatibility import python_2_unicode_compatible

from cmsplugin_filer_utils import FilerPluginManager
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
    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    source = FilerFileField(
        verbose_name=_('source'),
        null=True,
        on_delete=models.SET_NULL,
    )
    target_blank = models.BooleanField(_('Open link in new window'), default=False)
    style = models.CharField(
        _('Style'), choices=STYLE_CHOICES, default=DEFAULT_STYLE, max_length=255, blank=True)

    objects = FilerPluginManager(select_related=('source',))

    def get_icon_url(self):
        if self.source_id:
            return self.source.icons['32']
        return ''

    def file_exists(self):
        if self.source_id:
            return self.source.file.storage.exists(self.source.file.name)
        return False

    def get_file_name(self):
        if not self.source_id:
            return ''

        if self.file.name in ('', None):
            name = "%s" % (self.source.original_filename,)
        else:
            name = "%s" % (self.source.name,)
        return name

    def get_ext(self):
        return self.source.extension

    def __str__(self):
        if self.title:
            return self.title
        elif self.source_id:
            # added if, because it raised attribute error when file wasnt defined
            return self.get_file_name()
        return "<empty>"

    search_fields = ('title',)
