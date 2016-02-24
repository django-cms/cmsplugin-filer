# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0004_auto_20160120_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerimage',
            name='free_link',
            field=models.CharField(help_text='if present image will be clickable', max_length=2000, null=True, verbose_name='link', blank=True),
        ),
    ]
