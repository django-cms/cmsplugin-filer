# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_file', '0004_auto_20160705_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerfile',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_filer_file_filerfile', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
