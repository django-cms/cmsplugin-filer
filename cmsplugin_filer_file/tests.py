#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerFileTestCase(BasePluginTestMixin,
                                 CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerFilePlugin'

    def get_plugin_params(self):
        return {'file': self.get_filer_file_object()}
