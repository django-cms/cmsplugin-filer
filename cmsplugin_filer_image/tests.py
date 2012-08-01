#-*- coding: utf-8 -*-
from django.utils import unittest
from django.test.client import RequestFactory

class ContextTests(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def test_context_is_updated_not_replaced(self):
        from cmsplugin_filer_image.cms_plugins import FilerImagePlugin
        request = self.factory.get('/customer/details')
        context = {'my_test_variable': 42}
        new_context = FilerImagePlugin().render(context, request)
        self.assertIn('my_request_variable', new_context)

