# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0003_mv_thumbnail_option_to_filer_20160119_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerimage',
            name='thumbnail_option',
            field=models.ForeignKey(blank=True, to='filer.ThumbnailOption', help_text='overrides width, height, crop and upscale with values from the selected thumbnail option', null=True, verbose_name='thumbnail option'),
        ),
        migrations.DeleteModel(
            name='ThumbnailOption',
        ),
    ]
