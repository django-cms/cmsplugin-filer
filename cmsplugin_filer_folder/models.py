from __future__ import unicode_literals

import warnings
from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from filer.fields.folder import FilerFolderField
from filer.utils.compatibility import python_2_unicode_compatible
from .conf import settings
from cmsplugin_filer_utils import FilerPluginManager


@python_2_unicode_compatible
class FilerFolder(CMSPlugin):
    """
    Plugin for storing any type of Folder.

    Default template displays files store inside this folder.
    """
    STYLE_CHOICES = settings.CMSPLUGIN_FILER_FOLDER_STYLE_CHOICES
    DEFAULT_STYLE = settings.CMSPLUGIN_FILER_FOLDER_DEFAULT_STYLE
    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    folder = FilerFolderField()
    style = models.CharField(
        _('Style'), choices=STYLE_CHOICES, default=DEFAULT_STYLE, max_length=50)

    objects = FilerPluginManager(select_related=('folder',))

    @property
    def view_option(self):
        warnings.warn("view_option on cmsplugin_filer_folder.FilderFolder is deprecated. Use .style instead.",
                      DeprecationWarning)
        return self.style

    def __str__(self):
        if self.title:
            return self.title
        elif self.folder.name:
            # added if, because it raised attribute error when file wasnt defined
            return self.folder.name
        return "<empty>"

    search_fields = ('title',)
