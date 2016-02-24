# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0002_auto_20160108_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='mailto',
            field=models.EmailField(help_text='An email address has priority over both pages and urls', max_length=254, null=True, verbose_name='mailto', blank=True),
        ),
    ]
