from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page
from django.utils.translation import ugettext_lazy as _
from posixpath import join, basename, splitext, exists
from filer.fields.folder import FilerFolderField
from django.conf import settings


class FilerFolder(CMSPlugin):
    """
    Plugin for storing any type of Folder.
    
    Default template displays files store inside this folder.
    """
    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    folder = FilerFolderField()
    
        
    def __unicode__(self):
        if self.title: 
            return self.title;
        elif self.folder.name:
            # added if, because it raised attribute error when file wasnt defined
            return self.folder.name;
        return "<empty>"

    search_fields = ('title',)
    