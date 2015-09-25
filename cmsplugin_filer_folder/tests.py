# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from filer.models import Folder

from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerFolderTestCase(BasePluginTestMixin,
                                   CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerFolderPlugin'

    def get_plugin_params(self):
        folder = Folder(name='test_plugin', parent=None)
        folder.save()
        return {'folder': folder}
