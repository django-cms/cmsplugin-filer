# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError

from django.utils.translation import override

from cms import api
from filer.models import Image
from filer.models import ThumbnailOption
from cmsplugin_filer_image.models import FilerImage
from cmsplugin_filer_image.integrations.ckeditor import create_image_plugin

from cmsplugin_filer_tests_shared.base import (
    BasePluginTestMixin, CmsPluginsFilerBaseTestCase,
)


class CmsPluginFilerImageTestCase(BasePluginTestMixin,
                                  CmsPluginsFilerBaseTestCase):
    plugin_to_test = 'FilerImagePlugin'
    filer_class = Image

    def get_plugin_params(self):
        return {'image': self.get_filer_object()}

    def tearDown(self):
        super(CmsPluginFilerImageTestCase, self).tearDown()
        ThumbnailOption.objects.all().delete()

    def test_cms_plugin_icon_src_no_options(self):
        # plugin model
        image_plugin = self.create_plugin()
        plugin_instance = image_plugin.get_plugin_instance()[1]
        thumbnail = plugin_instance.icon_src(image_plugin)
        # assert that thumbnail url length is greater then '/media/'
        self.assertGreater(len(thumbnail), 7)

    def test_cms_plugin_icon_src_with_options(self):
        image_plugin = self.create_plugin()
        # prepare options
        option_kwargs = {
            'name': 'Default thumbnail 175x175 crop upscale',
            'width': 175,
            'height': 175,
            'crop': True,
            'upscale': True,
        }
        thumbnail_option = ThumbnailOption(**option_kwargs)
        thumbnail_option.save()

        image_plugin.thumbnail_option = thumbnail_option
        image_plugin.save()
        image_plugin = self.refresh(image_plugin)
        # actual test
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

    def test_create_image_plugin(self):
        placeholder = self.page.placeholders.all()[0]
        text_plugin = api.add_plugin(
            placeholder, 'TextPlugin', 'en')
        self.page.publish('en')

        # create filer image,
        filename = 'test_integration.jpg'
        image = self.get_django_file_object(filename)

        # invoke create_image_plugin
        image_plugin = create_image_plugin(
            filename, image, text_plugin)

        # assert returned plugin is not none, class image plugin =)
        self.assertTrue(image_plugin, FilerImage)

        # cms 3.1 has get_parent method, use it if we testing against 3.1
        if hasattr(image_plugin, 'get_parent'):
            parent = image_plugin.get_parent()
        else:
            # fall back for cms 3.0
            parent = image_plugin.parent
        self.assertEqual(parent, text_plugin.cmsplugin_ptr)

    def test_clean(self):
        image_plugin = FilerImage()
        with self.assertRaises(ValidationError):
            image_plugin.clean()
        filer_image = self.get_filer_object()
        image_plugin.image = filer_image
        image_plugin.image_url = 'https://github.com/divio/django-cms'
        with self.assertRaises(ValidationError):
            image_plugin.clean()
