# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from filer.models.imagemodels import Image
from easy_thumbnails.files import ThumbnailFile

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
            'free_link': 'https://github.com/divio/cmsplugin-filer'}

    def test_get_thumbnail(self):
        teaser_plugin = self.create_plugin()
        plugin_instance = teaser_plugin.get_plugin_instance()[1]
        thumbnail = plugin_instance.get_thumbnail({}, teaser_plugin)
        self.assertTrue(isinstance(thumbnail, ThumbnailFile))
