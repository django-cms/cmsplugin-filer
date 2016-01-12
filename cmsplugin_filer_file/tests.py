# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import force_text

from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerFileTestCase(BasePluginTestMixin,
                                 CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerFilePlugin'

    def get_plugin_params(self):
        return {'file': self.get_filer_object()}

    def test_no_file(self):
        filer_file_plugin = self._create_plugin(file=None)
        self.assertEqual(filer_file_plugin.get_file_name(), '')
        self.assertEqual(filer_file_plugin.get_icon_url(), '')
        self.assertEqual(force_text(filer_file_plugin), '<empty>')

    def test_get_file_name(self):
        filer_file_plugin = self.create_plugin()
        # check with original file name
        self.assertEqual(filer_file_plugin.get_file_name(), 'test_file.jpg')
        # test with file name
        filer_file_plugin.file.name = 'new_test_file_name.jpg'
        filer_file_plugin.file.save()
        filer_file_plugin = filer_file_plugin._meta.model.objects.get(
            pk=filer_file_plugin.pk)
        self.assertEqual(filer_file_plugin.get_file_name(), 'new_test_file_name.jpg')

    def test_file_exists(self):
        filer_file_plugin = self.create_plugin()
        self.assertTrue(filer_file_plugin.file_exists())
        filer_file_plugin.file.file.delete()
        self.assertFalse(filer_file_plugin.file_exists())

    def test_get_ext(self):
        filer_file_plugin = self.create_plugin()
        self.assertEqual(filer_file_plugin.get_ext(), 'jpg')

    def test_str(self):
        filer_file_plugin = self.create_plugin()
        self.assertEqual(force_text(filer_file_plugin), 'test_file.jpg')
        filer_file_plugin.title = 'New title for file'
        filer_file_plugin.save()
        filer_file_plugin = filer_file_plugin._meta.model.objects.get(
            pk=filer_file_plugin.pk)
        self.assertEqual(force_text(filer_file_plugin), 'New title for file')
