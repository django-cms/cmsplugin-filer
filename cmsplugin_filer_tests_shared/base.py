# -*- coding: utf-8 -*-

from django.conf import settings
from django.test import TransactionTestCase
from django.utils.translation import override

from cms import api
from cms.utils import get_cms_setting


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
            page = self.root_page
        if language is None:
            language = 'en'

        placeholder = page.placeholders.all()[0]
        plugin = api.add_plugin(
            placeholder, self.plugin_to_test, language, **plugin_params)
        page.publish(language)
        return plugin

    def create_plugin(self, page=None, language=None, **kwargs):
        """
        Create plugin on a page, use this to provide additional actions or
        settings if needed.
        """
        plugin_args = {}
        plugin_args.update(self.plugin_params)
        if kwargs:
            plugin_args.update(kwargs)
        return self._create_plugin(**plugin_args)

    def test_plugin_can_be_added(self):
        plugin = self.create_plugin()
        self.assertTrue(plugin is not None)
        self.assertIn(plugin, self.page.placeholders.all()[0].get_plugins())

    def test_plugin_does_not_breakes_page(self):
        with override('en'):
            page_url = self.root_page.get_absolute_url()

        response = self.client.get(page_url)
        self.assertEqual(response.status_code, 200)


class CmsPluginsFilerBaseTestCase(TransactionTestCase):

    def setUp(self):
        super(CmsPluginsFilerBaseTestCase, self).setUp()
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.root_page = self.create_root_page()
        self.placeholder = self.root_page.placeholders.all()[0]

    def create_root_page(self):
        root_page = api.create_page(
            'root page', self.template, self.language, published=True)
        api.create_title('de', 'root page de', root_page)
        root_page.publish('en')
        root_page.publish('de')
        return root_page.reload()
