# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms

from djangocms_attributes_field.widgets import AttributesWidget

from .models import FilerLink2Plugin


class FilerLink2Form(forms.ModelForm):

    class Meta:
        model = FilerLink2Plugin
        exclude = []
        readonly_fields = ('persistent_page_link',)

    def __init__(self, *args, **kwargs):
        super(FilerLink2Form, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget()
