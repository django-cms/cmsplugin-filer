# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms

from djangocms_attributes_field.widgets import AttributesWidget

from .models import FilerLinkPlugin


class FilerLinkForm(forms.ModelForm):

    class Meta:
        model = FilerLinkPlugin
        exclude = []

    def __init__(self, *args, **kwargs):
        super(FilerLinkForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget()
