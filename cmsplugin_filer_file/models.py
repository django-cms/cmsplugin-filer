from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page
from django.utils.translation import ugettext_lazy as _
from posixpath import join, basename, splitext, exists
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.conf import settings
from cmsplugin_filer_utils import FilerPluginManager


class FilerFile(CMSPlugin):
    """
    Plugin for storing any type of file.

    Default template displays download link with icon (if available) and file size.

    Icons are searched for within <MEDIA_ROOT>/<CMS_FILE_ICON_PATH>
    (CMS_FILE_ICON_PATH is a plugin-specific setting which defaults to "<CMS_MEDIA_PATH>/images/file_icons")
    with filenames of the form <file_ext>.<icon_ext>, where <file_ext> is the extension
    of the file itself, and <icon_ext> is one of <CMS_FILE_ICON_EXTENSIONS>
    (another plugin specific setting, which defaults to ('gif', 'png'))

    This could be updated to use the mimetypes library to determine the type of file rather than
    storing a separate icon for each different extension.

    The icon search is currently performed within get_icon_url; this is probably a performance concern.
    """
    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    file = FilerFileField(verbose_name=_('file'))

    objects = FilerPluginManager(select_related=('file',))

    def get_icon_url(self):
        return self.file.icons['32']

    def file_exists(self):
        return exists(self.file.path);

    def get_file_name(self):
        return basename(self.file.path)

    def get_ext(self):
        return splitext(self.get_file_name())[1][1:]

    def __unicode__(self):
        if self.title:
            return self.title;
        elif self.file:
            # added if, because it raised attribute error when file wasnt defined
            return self.get_file_name();
        return "<empty>"

    search_fields = ('title',)
