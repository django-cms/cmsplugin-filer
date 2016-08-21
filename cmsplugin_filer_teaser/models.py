from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField
from filer.fields.image import FilerImageField
from filer.utils.compatibility import python_2_unicode_compatible
from .conf import settings
from cmsplugin_filer_utils import FilerPluginManager


@python_2_unicode_compatible
class FilerTeaser(CMSPlugin):
    """
    A Teaser
    """
    STYLE_CHOICES = settings.CMSPLUGIN_FILER_TEASER_STYLE_CHOICES
    DEFAULT_STYLE = settings.CMSPLUGIN_FILER_TEASER_DEFAULT_STYLE
    title = models.CharField(_("title"), max_length=255, blank=True)
    image = FilerImageField(
        blank=True,
        null=True,
        verbose_name=_("image"),
        on_delete=models.SET_NULL,
    )
    image_url = models.URLField(_("alternative image url"), null=True, blank=True, default=None)
    style = models.CharField(
        _('Style'), choices=STYLE_CHOICES, default=DEFAULT_STYLE, max_length=255, blank=True)
    use_autoscale = models.BooleanField(_("use automatic scaling"), default=True,
                                        help_text=_('tries to auto scale the image based on the placeholder context'))
    width = models.PositiveIntegerField(_("width"), null=True, blank=True)
    height = models.PositiveIntegerField(_("height"), null=True, blank=True)

    free_link = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    page_link = PageField(
        null=True,
        blank=True,
        help_text=_("if present image will be clickable"),
        verbose_name=_("page link"),
        on_delete=models.SET_NULL,
    )
    description = models.TextField(_("description"), blank=True, null=True)

    target_blank = models.BooleanField(_("open link in new window"), default=False)

    cmsplugin_ptr = models.OneToOneField(
        to=CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    objects = FilerPluginManager(select_related=('image', 'page_link'))

    def clean(self):
        from django.core.exceptions import ValidationError
        # Make sure that either image or image_url is set
        if self.image and self.image_url:
            raise ValidationError(_('Either an image or an image url must be selected.'))

    def __str__(self):
        return self.title

    @property
    def link(self):
        try:
            if self.free_link:
                return self.free_link
            elif self.page_link and self.page_link:
                return self.page_link.get_absolute_url()
            else:
                return ''
        except Exception as e:
            print(e)
