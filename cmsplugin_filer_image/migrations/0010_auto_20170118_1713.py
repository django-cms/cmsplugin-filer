# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0009_auto_20160713_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerimage',
            name='attribution_text',
            field=models.CharField(max_length=255, null=True, verbose_name='attribution text', blank=True),
        ),
        migrations.AddField(
            model_name='filerimage',
            name='caption_alignment',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='caption alignment', choices=[('left', 'left'), ('right', 'right')]),
        ),
    ]
