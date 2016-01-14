# -*- coding: utf-8 -*-
from django.conf import settings  # NOQA
from django.utils.translation import ugettext_lazy as _
from appconf import AppConf


class CmspluginFilerFolderAppConf(AppConf):
    STYLE_CHOICES = (
        ("list", _("List")),
        ("slideshow", _("Slideshow"))
    )
    DEFAULT_STYLE = 'list'

    def configure(self):
        # set DEFAULT_STYLE to '' if it is not in STYLE_CHOICES
        if not self.configured_data['DEFAULT_STYLE'] in [s for s, l in self.configured_data['STYLE_CHOICES']]:
            self.configured_data['DEFAULT_STYLE'] = ''
        return self.configured_data
