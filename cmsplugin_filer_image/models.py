import django
from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from cmsplugin_filer_utils import FilerPluginManager
from distutils.version import LooseVersion
from django.core.exceptions import ValidationError


class ThumbnailOptionManager(models.Manager):

    IMG_MAX_WIDTH = 1024
    DEFAULT_WIDTHS = [{'name': 'Small', 'width': 180},
                      {'name': 'Medium', 'width': 320},
                      {'name': 'Large', 'width': 616}]

    def get_default_options(self, filer_image):
        result = []
        defaults_others = {'height': 0, 'crop': False, 'upscale': False}

        for defaults in self.DEFAULT_WIDTHS:
            if not filer_image or filer_image.width > defaults['width']:
                defaults.update(defaults_others)
                result.append(self.get_or_create(**defaults)[0].id)

        if filer_image:
            if filer_image.width < self.IMG_MAX_WIDTH:
                # A 720x405 image would result in the following options:
                # Original: 720x405
                # Large: 6160x360
                # Medium: 320X180
                # Small: 180x101
                defaults_others['height'] = filer_image.height
                original_width = filer_image.width
            else:
                # A 1920x1080px image would result in the following options:
                # Original: 1024x576
                # Large: 616x360
                # Medium: 320X180
                # Small: 180x101
                aspect_ratio = float(filer_image.width) / filer_image.height
                defaults_others['height'] = int(self.IMG_MAX_WIDTH / aspect_ratio)
                original_width = self.IMG_MAX_WIDTH
        else:
            original_width = self.IMG_MAX_WIDTH

        # the height is set only for the Original thumbnail option and
        #  not for the others (Large, Small, Medium), thus minimising
        #  the number of objects created in the db
        result.append(self.get_or_create(
            name='Original', width=original_width, **defaults_others)[0].id)

        return self.filter(id__in=result)


class ThumbnailOption(models.Model):
    """
    This class defines the option use to create the thumbnail.
    """
    name = models.CharField(_("name"), max_length=100)
    width = models.IntegerField(_("width"), help_text=_('width in pixel.'))
    height = models.IntegerField(_("height"), help_text=_('height in pixel.'))
    crop = models.BooleanField(_("crop"), default=True)
    upscale = models.BooleanField(_("upscale"), default=True)

    objects = ThumbnailOptionManager()

    class Meta:
        ordering = ('-width', )
        verbose_name = _("thumbnail option")
        verbose_name_plural = _("thumbnail options")

    def __unicode__(self):
        return u'%s -- %s x %s' % (self.name,
                                   self.width,
                                   self.height or 'XXX')

    @property
    def as_dict(self):
        """
        This property returns a dictionary suitable for Thumbnailer.get_thumbnail()

        Sample code:
            # thumboption_obj is a ThumbnailOption instance
            # filerimage is a Image instance
            option_dict = thumboption_obj.as_dict
            thumbnailer = filerimage.easy_thumbnails_thumbnailer
            thumb_image = thumbnailer.get_thumbnail(option_dict)
        """
        return {"size": (self.width, self.height),
                "width": self.width,
                "height": self.height,
                "crop": self.crop,
                'upscale': self.upscale,
        }


class FilerImage(CMSPlugin):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    FLOAT_CHOICES = (
        (CENTER, _("center")),
        (LEFT, _("left")),
        (RIGHT, _("right")),
    )
    DEFAULT_HORIZONTAL_SPACE = 15
    DEFAULT_VERTICAL_SPACE = 15

    OPT_NO_LINK = 1
    OPT_ADD_LINK = 2
    OPT_PAGE_LINK = 3
    OPT_FILE_LINK = 4
    OPT_ORIGINAL_IMG_LINK = 5

    ##
    alt_text = models.CharField(
        _("alt text"), null=True,
        blank=True, max_length=255,
        help_text=_("Describes the essence of the image for users who have images "
                    "turned off in their browser, or are visually impaired and using "
                    "a screen reader; and it is useful to identify images to search "
                    "engines"))
    caption_text = models.CharField(
        _("caption text"), null=True,
        blank=True, max_length=140,
        help_text=_("Caption text is displayed directly below an image to add context; "
                    "there is a 140-character limit, including spaces; for images "
                    "fewer than 200 pixels wide, the caption text is only displayed "
                    "on hover"))
    credit_text = models.CharField(
        _("credit text"), null=True,
        blank=True, max_length=30,
        help_text=_("Credit text gives credit to the owner or licensor of an image; "
                    "it is displayed below the image,<br>or below the caption text if "
                    "that option is selected; there is a 30-character limit, "
                    "including spaces."))
    show_caption = models.BooleanField(
        _("show caption text"), default=False)
    show_credit = models.BooleanField(
        _("show credit text"), default=False)

    image = FilerImageField(
        null=True, blank=True, on_delete=models.SET_NULL,
        default=None, verbose_name=_("image"))

    ##Image Options
    thumbnail_option = models.ForeignKey(
        'ThumbnailOption', null=True,
        blank=True, verbose_name=_("image size"),
        on_delete=models.SET_NULL,
        help_text=_("The most common image options are available via this drop-down"
                    " menu; to add a custom size, use the advanced options menu "
                    "below; any advanced option selection will override the "
                    "settings in this admin."))

    alignment = models.CharField(
        _("image alignment"), max_length=10,
        blank=True, null=True,
        choices=FLOAT_CHOICES,
        help_text=_("When inside a text plugin, text will wrap around images "
                    "with a left or right alignment; text will not wrap "
                    "around an image with a center alignment."))

    link_options = models.IntegerField(
        _('link image options'),
        default=1, choices=(
            (OPT_NO_LINK, "No link"),
            (OPT_ADD_LINK, "Add link"),
            (OPT_PAGE_LINK, "Link to page"),
            (OPT_FILE_LINK, "Link to document/media"),
            (OPT_ORIGINAL_IMG_LINK, "Open original image in overlay"),
        ),
        help_text=_("This menu provieds options for linking the image to "
                    "another file, another page, a document, or to open "
                    "up the image in its original size; making a "
                    "selection via the dropdown will generate the "
                    " required admin fields.")
    )
    free_link = models.CharField(
        _("link"), max_length=255, blank=True,
        null=True, help_text=_("if present image will be clickable"))
    target_blank = models.BooleanField(
        _('Open link in new window'), default=False)
    page_link = PageField(
        null=True,  blank=True,
        help_text=_("if present image will be clickable"),
        verbose_name=_("page link"))
    file_link = FilerFileField(
        null=True, blank=True, on_delete=models.SET_NULL,
        default=None, verbose_name=_("file link"),
        help_text=_("if present image will be clickable"),
        related_name='+')

    ## Advanced
    width = models.PositiveIntegerField(
        _("width"), null=True, blank=True)
    height = models.PositiveIntegerField(
        _("height"), null=True, blank=True)
    crop = models.BooleanField(
        _("crop"), default=False)
    maintain_aspect_ratio = models.BooleanField(
        _("maintain aspect ratio"), default=True)

    vertical_space = models.PositiveIntegerField(
        _("vertical space"), null=True, blank=True)
    horizontal_space = models.PositiveIntegerField(
        _("horizontal space"), null=True, blank=True,
        help_text=_('Add spacing or padding around the image; calculated in pixels; if left blank, the vertical spacing will default to 15 pixels.'))
    border = models.PositiveIntegerField(
        _("border"), null=True, blank=True,
        help_text=_("Add a black border around the image; the input is the pixel width of the line; there is no line if left blank.")
    )

    ## Deprecated fields. kept for backward compatibility
    ## to be removed at some point in time
    upscale = models.BooleanField(_("upscale"), default=True)
    description = models.TextField(
        _("description"), blank=True, null=True)

    use_original_image = models.BooleanField(
        _("use the original image"), default=False,
        help_text=_('do not resize the image. use the original image instead.'))

    original_link = models.BooleanField(
        _("link original image"), default=False,
        help_text=_("if present image will be clickable"))
    use_autoscale = models.BooleanField(
        _("use automatic scaling"), default=False,
        help_text=_('tries to auto scale the image based on the placeholder context'))

    # we only add the image to select_related. page_link and file_link are FKs
    # as well, but they are not used often enough to warrant the impact of two
    # additional LEFT OUTER JOINs.
    objects = FilerPluginManager(select_related=('image',))

    class Meta:
        verbose_name = _("filer image")
        verbose_name_plural = _("filer images")

    def clean(self):
        # Make sure that either image or image_url is set
        if not self.image:
            raise ValidationError(_('An image must be selected.'))

    def __unicode__(self):
        if self.image:
            return self.image.label
        else:
            return unicode( _("Image Publication %(caption)s") % {'caption': self.caption or self.alt} )
        return ''

    @property
    def caption(self):
        if self.image:
            return self.caption_text or self.image.default_caption
        else:
            return self.caption_text

    @property
    def credit(self):
        if self.image:
            return self.credit_text or self.image.default_credit
        else:
            return self.credit_text

    @property
    def alt(self):
        if self.image:
            return self.alt_text or self.image.default_alt_text or self.image.label
        else:
            return self.alt_text

    @property
    def link(self):
        if self.link_options == self.OPT_ADD_LINK:
            return self.free_link
        elif self.link_options == self.OPT_PAGE_LINK:
            return self.page_link.get_absolute_url()
        elif self.link_options == self.OPT_FILE_LINK and self.file_link:
            return self.file_link.url
        elif self.link_options == self.OPT_ORIGINAL_IMG_LINK and self.image:
            return self.image.url
        else:
            return ''

    @property
    def vert_space(self):
        return self.vertical_space

    @property
    def horiz_space(self):
        return self.horizontal_space

    @property
    def style(self):
        style = ""
        if self.alignment == self.CENTER:
            style += 'margin: auto; display: block;'
        else:
            style += "float: %s;" % self.alignment if self.alignment else ""
            if self.alignment == self.LEFT:
                style += "margin-right: %spx;" % self.DEFAULT_HORIZONTAL_SPACE
            if self.alignment == self.RIGHT:
                style += "margin-left: %spx;" % self.DEFAULT_HORIZONTAL_SPACE

        if isinstance(self.vertical_space, (int, long)):
            style += "margin-top: %spx; margin-bottom: %spx;" % (
                self.vert_space, self.vert_space)

        if not self.alignment == self.CENTER and isinstance(self.horiz_space, (int, long)):
            style += "margin-right: %spx; margin-left: %spx;" % (
                self.horiz_space, self.horiz_space)

        style += "border: %spx solid black;" % self.border if self.border else ""
        return style
