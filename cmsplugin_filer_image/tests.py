#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import override
from filer.models import Image
from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerImageTestCase(BasePluginTestMixin,
                                  CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerImagePlugin'
    filer_class = Image

    def get_plugin_params(self):
        return {'image': self.get_filer_object()}

    def test_cms_plugin_icon_src(self):
        # plugin model
        image_plugin = self.create_plugin()
        plugin_instance = image_plugin.get_plugin_instance()[1]
        thumbnail = plugin_instance.icon_src(image_plugin)
        # assert that thumbnail url length is greater then '/media/'
        self.assertGreater(len(thumbnail), 7)

    def test_link_property(self):
        image_plugin = self.create_plugin()
        # empty link
        self.assertEqual(len(image_plugin.link), 0)

        # original link is used
        image_plugin.original_link = True
        image_plugin.save()
        image_plugin = self.refresh(image_plugin)
        self.assertEqual(image_plugin.link, image_plugin.image.url)
        # file link has higher priority over original_link
        other_django_file = self.get_django_file_object('another_image.jpg')
        other_filer_file = self.get_filer_object(file_obj=other_django_file)
        image_plugin.file_link = other_filer_file
        image_plugin.save()
        image_plugin = self.refresh(image_plugin)
        self.assertEqual(image_plugin.link, other_filer_file.url)

        # page link should be higher prio
        image_plugin.page_link = self.page
        image_plugin.save()
        image_plugin = self.refresh(image_plugin)
        with override('en'):
            self.assertEqual(image_plugin.link, self.page.get_absolute_url())

        # free link should be the highest
        cms_github_link = 'https://github.com/divio/django-cms'
        image_plugin.free_link = cms_github_link
        image_plugin.save()
        image_plugin = self.refresh(image_plugin)
        self.assertEqual(image_plugin.link, cms_github_link)