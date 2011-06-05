from cms.models import CMSPlugin
from cmsplugin_filer_video import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from os.path import basename
import re

class FilerVideo(CMSPlugin):
    # player settings
    movie = FilerFileField(verbose_name=_('movie file'), help_text=_('use .flv file or h264 encoded video file'), blank=True, null=True)
    movie_url = models.CharField(_('movie url'), max_length=255, help_text=_('vimeo or youtube video url. Example: http://www.youtube.com/watch?v=YFa59lK-kpo'), blank=True, null=True)
    image = FilerImageField(verbose_name=_('image'), help_text=_('preview image file'), null=True, blank=True, related_name='filer_video_image')
    
    width = models.PositiveSmallIntegerField(_('width'), default=settings.VIDEO_WIDTH)
    height = models.PositiveSmallIntegerField(_('height'), default=settings.VIDEO_HEIGHT)
    
    auto_play = models.BooleanField(_('auto play'), default=settings.VIDEO_AUTOPLAY)
    auto_hide = models.BooleanField(_('auto hide'), default=settings.VIDEO_AUTOHIDE)
    fullscreen = models.BooleanField(_('fullscreen'), default=settings.VIDEO_FULLSCREEN)
    loop = models.BooleanField(_('loop'), default=settings.VIDEO_LOOP)
    
    # plugin settings
    bgcolor = models.CharField(_('background color'), max_length=6, default=settings.VIDEO_BG_COLOR, help_text=_('Hexadecimal, eg ff00cc'))
    textcolor = models.CharField(_('text color'), max_length=6, default=settings.VIDEO_TEXT_COLOR, help_text=_('Hexadecimal, eg ff00cc'))
    seekbarcolor = models.CharField(_('seekbar color'), max_length=6, default=settings.VIDEO_SEEKBAR_COLOR, help_text=_('Hexadecimal, eg ff00cc'))
    seekbarbgcolor = models.CharField(_('seekbar bg color'), max_length=6, default=settings.VIDEO_SEEKBARBG_COLOR, help_text=_('Hexadecimal, eg ff00cc'))
    loadingbarcolor = models.CharField(_('loadingbar color'), max_length=6, default=settings.VIDEO_LOADINGBAR_COLOR, help_text=_('Hexadecimal, eg ff00cc'))
    buttonoutcolor = models.CharField(_('button out color'), max_length=6, default=settings.VIDEO_BUTTON_OUT_COLOR, help_text=_('Hexadecimal, eg ff00cc'))
    buttonovercolor = models.CharField(_('button over color'), max_length=6, default=settings.VIDEO_BUTTON_OVER_COLOR, help_text=_('Hexadecimal, eg ff00cc'))        
    buttonhighlightcolor = models.CharField(_('button highlight color'), max_length=6, default=settings.VIDEO_BUTTON_HIGHLIGHT_COLOR, help_text=_('Hexadecimal, eg ff00cc'))
    
        
    def __unicode__(self):
        if self.movie:
            name = self.movie.path
        else:
            name = self.movie_url
        return u"%s" % basename(name)

    def get_height(self):
        return "%s" % (self.height)
    
    def get_width(self):
        return "%s" % (self.width)    
    
    def get_movie(self):
        if self.movie:
            return self.movie.url
        else:
            return self.movie_url

