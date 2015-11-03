# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from filer.models.imagemodels import Image

from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerVideoTestCase(BasePluginTestMixin,
                                  CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerVideoPlugin'
    filer_class = Image

    def get_plugin_params(self):
        return {
            'movie_url': 'https://vimeo.com/channels/952478/133154447',
            'image': self.get_filer_object(),
        }
