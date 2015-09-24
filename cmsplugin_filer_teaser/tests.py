# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from filer.models.imagemodels import Image

from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerTeaserTestCase(BasePluginTestMixin,
                                 CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerTeaserPlugin'
    filer_class = Image

    def get_plugin_params(self):
        return {
            'title': 'test teaser!',
            'image': self.get_filer_object(),
            'free_link': 'https://github.com/stefanfoulis/cmsplugin-filer'}