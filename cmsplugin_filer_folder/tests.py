# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tempfile import mkstemp

from django.contrib.auth.models import AnonymousUser
from django.utils.encoding import force_text

from filer.models import Folder, File, Image
from django.core.files import File as DjangoFile

from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerFolderTestCase(BasePluginTestMixin,
                                   CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerFolderPlugin'

    def test_no_folder(self):
        filer_folder_plugin = self._create_plugin(folder=None)
        self.assertEqual(force_text(filer_folder_plugin), '<empty>')

    def get_plugin_params(self):
        folder = Folder(name='test_plugin', parent=None)
        folder.save()
        return {'folder': folder}

    def test_select_files(self):
        folder = Folder.objects.create(name='test')
        obj1 = self.get_filer_object(filer_class=Image)
        obj1.folder = folder
        obj1.save()
        __, filepath = mkstemp()
        file_obj = DjangoFile(open(filepath, 'rb'), name='test_file')
        obj2 = self.get_filer_object(filer_class=File, file_obj=file_obj)
        obj2.folder = folder
        obj2.save()
        filer_folder_plugin = self._create_plugin(folder=folder)
        plugin = filer_folder_plugin.get_plugin_class_instance()
        files = plugin.get_folder_files(folder, AnonymousUser())
        self.assertEqual(files.count(), 1)
        imgs = plugin.get_folder_images(folder, AnonymousUser())
        self.assertEqual(imgs.count(), 1)
        self.assertFalse(imgs[0] == files[0])
