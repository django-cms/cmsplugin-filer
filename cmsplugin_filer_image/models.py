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

    def get_default_options_ids(self):
        result = []
        defaults = {'height': 0, 'crop': False, 'upscale': False}
        result.append(ThumbnailOption.objects.get_or_create(
            name='Small', width=180, **defaults)[0].id)
        result.append(ThumbnailOption.objects.get_or_create(
            name='Medium', width=320, **defaults)[0].id)
        result.append(ThumbnailOption.objects.get_or_create(
            name='Large', width=640, **defaults)[0].id)
        result.append(ThumbnailOption.objects.get_or_create(
            name='Original', width=1024, **defaults)[0].id)

        return result


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
        return u'%s -- %s x %s' %(self.name, self.width, self.height or 'XXX')

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
                "maintain_aspect_ratio": self.maintain_aspect_ratio}


class FilerImage(CMSPlugin):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    FLOAT_CHOICES = (
        (CENTER, _("center")),
        (LEFT, _("left")),
        (RIGHT, _("right")),
    )

    ##
    alt_text = models.CharField(
        _("alt text"), null=True,
        blank=True, max_length=255,
        help_text=_("Provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader)"))
    caption_text = models.CharField(
        _("caption text"), null=True,
        blank=True, max_length=255,
        help_text=_("Used to create a tooltip for an image "))
    credit_text = models.CharField(
        _("credit text"), null=True,
        blank=True, max_length=255,
        help_text=_("tbd"))
    show_alt = models.BooleanField(
        _("show alt text"), default=False)
    show_caption = models.BooleanField(
        _("show caption text"), default=False)
    show_credit = models.BooleanField(
        _("show credit text"), default=False)

    image = FilerImageField(
        null=True, blank=True,
        default=None, verbose_name=_("image"))

    ##Image Options
    thumbnail_option = models.ForeignKey(
        'ThumbnailOption', null=True,
        blank=True, verbose_name=_("image size"),
        limit_choices_to={'id__in': ThumbnailOption.objects.get_default_options_ids()})

    alignment = models.CharField(
        _("image alignment"), max_length=10,
        blank=True, null=True,
        choices=FLOAT_CHOICES)

    link_options = models.IntegerField(
        _('link image options'),
        default=1, choices=(
            (1, "No link"),
            (2, "Add link"),
            (3, "Link to page"),
            (4, "Link to document/media"),
            (5, "Open original image in overlay"),
        )
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
        null=True, blank=True,
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
        help_text=_('Add spacing or padding around the image; calculated in pixels; if left blank, the spacing will default to 15 pixels.'))
    border = models.PositiveIntegerField(
        _("border"), null=True, blank=True,
        help_text=_("Add a black border around the image; the input is the pixel width of the line; there is no line if left blank.")
    )

    ## Not used anymore but kept for backward compatibility
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
        if self.link_options == 2:
            return self.free_link
        elif self.link_options == 3:
            return self.page_link.get_absolute_url()
        elif self.link_options == 4:
            return self.file_link.url
        elif self.link_options == 5:
            return self.image.url
        else:
            return ''

    @property
    def style(self):
        style = ""
        if self.alignment == self.CENTER:
            style += 'margin: auto; display: block;'
        else:
            style += "float: %s;" % self.alignment if self.alignment else ""

        if self.vertical_space:
            style += "margin-top: %spx; margin-bottom: %spx;" % (self.vertical_space, self.vertical_space)
        elif self.horizontal_space and not self.alignment == self.CENTER:
            style += "margin-right: %spx; margin-left: %spx;" % (self.horizontal_space, self.horizontal_space)

        style += "border: %spx solid black;" % self.border if self.border else ""
        return style
