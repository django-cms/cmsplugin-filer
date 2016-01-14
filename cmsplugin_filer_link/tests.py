# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerLinkTestCase(BasePluginTestMixin,
                                 CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerLinkPlugin'

    def get_plugin_params(self):
        params = {
            'name': 'test link',
            'url': 'https://github.com/divio/cmsplugin-filer',
            'file': self.get_filer_object(),
            'page_link': self.root_page,
        }
        return params
