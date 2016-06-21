# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0006_auto_20160427_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerimage',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(help_text='Optional. Adds HTML attributes to the rendered link.', default=dict),
        ),
    ]
