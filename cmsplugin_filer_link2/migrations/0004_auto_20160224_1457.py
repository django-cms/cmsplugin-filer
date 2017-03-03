# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0003_auto_20160224_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='url',
            field=models.CharField(max_length=2000, null=True, verbose_name='url', blank=True),
        ),
    ]
