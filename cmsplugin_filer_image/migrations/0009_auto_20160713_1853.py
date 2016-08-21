# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0008_auto_20160705_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerimage',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_filer_image_filerimage', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
