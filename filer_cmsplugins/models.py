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
    file = FilerFileField()
    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    
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
    

'''
class FolderPublication(CMSPlugin):
    folder = ImageFilerModelFolderField()
'''
