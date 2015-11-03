# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.core.files import File as DjangoFile
from django.test import TransactionTestCase
from django.utils.translation import override

from cms import api
from cms.utils import get_cms_setting

from filer.models.filemodels import File
from filer.tests.helpers import create_image


class BasePluginTestMixin(object):
    plugin_to_test = 'TextPlugin'
    plugin_params = {}

    def _create_plugin(self, page=None, language=None, **plugin_params):
        """
        Create plugin of type self.plugin_to_test and plugin_params in
        given language to a page placeholder.
        Assumes that page has that translation.
        """
        if page is None:
            page = self.page
        if language is None:
            language = 'en'

        placeholder = page.placeholders.all()[0]
        plugin = api.add_plugin(
            placeholder, self.plugin_to_test, language, **plugin_params)
        page.publish(language)
        return plugin

    def get_plugin_params(self):
        params = {}
        params.update(self.plugin_params)
        return params

    def create_plugin(self, **kwargs):
        """
        Create plugin on a page, use this to provide additional actions or
        settings if needed.
        """
        plugin_args = self.get_plugin_params()
        if kwargs:
            plugin_args.update(kwargs)
        return self._create_plugin(**plugin_args)

    def test_plugin_can_be_added(self):
        plugin = self.create_plugin()
        self.assertTrue(plugin is not None)
        self.assertIn(plugin.cmsplugin_ptr,
                      self.page.placeholders.all()[0].get_plugins())

    def test_plugin_does_not_breakes_page(self):
        self.create_plugin()
        with override('en'):
            page_url = self.page.get_absolute_url()

        response = self.client.get(page_url)
        self.assertEqual(response.status_code, 200)


class CmsPluginsFilerBaseTestCase(TransactionTestCase):

    def setUp(self):
        super(CmsPluginsFilerBaseTestCase, self).setUp()
        # cms related
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.root_page = self.create_root_page()
        page = api.create_page(
            title='Plugins test en', template=self.template, language='en',
            published=True,
            parent=self.root_page,
        )
        page.publish('en')
        self.page = page.reload()

        self.placeholder = self.page.placeholders.all()[0]
        # filer related, taken from django-filer.tests test cases setUp logic
        self.image = create_image()
        self.image_name = 'test_file.jpg'
        self.filename = os.path.join(settings.FILE_UPLOAD_TEMP_DIR,
                                     self.image_name)
        self.image.save(self.filename, 'JPEG')

    def tearDown(self):
        self.client.logout()
        os.remove(self.filename)
        for f in File.objects.all():
            f.delete()
        super(CmsPluginsFilerBaseTestCase, self).tearDown()

    def get_django_file_object(self, name=None):
        """
        Creates django.code.files.File object and returns it, uses self.filename
        file (should exist) uses name to populate DjangoFile.name, if not
        provided uses self.image_name
        :return: django.code.files.File
        """
        if name is None:
            name = self.image_name
        file_obj = DjangoFile(open(self.filename, 'rb'), name=name)
        return file_obj

    def get_filer_object(self, filer_class=None, file_obj=None):
        if filer_class is None:
            filer_class = getattr(self, 'filer_class', File)
        if file_obj is None:
            file_obj = self.get_django_file_object()
        file_name = file_obj.name.split('/')[-1]
        filer_file_instance = filer_class(file=file_obj)
        # preserve filename
        filer_file_instance.original_filename = file_name
        filer_file_instance.save()
        return filer_file_instance

    def create_root_page(self):
        root_page = api.create_page(
            'root page', self.template, self.language, published=True)
        api.create_title('de', 'root page de', root_page)
        root_page.publish('en')
        root_page.publish('de')
        return root_page.reload()

    def refresh(self, instance):
        """
        Refresh instance from db using _meta.model
        """
        return instance._meta.model.objects.get(pk=instance.pk)
