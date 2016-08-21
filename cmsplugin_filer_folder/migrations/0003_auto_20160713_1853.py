# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_folder', '0002_auto_20160113_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerfolder',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_filer_folder_filerfolder', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
