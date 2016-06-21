# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0004_auto_20160224_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerlinkplugin',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, help_text='Optional. Adds HTML attributes to the rendered link.'),
        ),
    ]
