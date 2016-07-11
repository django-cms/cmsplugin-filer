# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms

from djangocms_attributes_field.widgets import AttributesWidget

from .models import FilerFile


class FilerFileForm(forms.ModelForm):

    class Meta:
        model = FilerFile
        exclude = []

    def __init__(self, *args, **kwargs):
        super(FilerFileForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget()
