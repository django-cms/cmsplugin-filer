# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filervideo',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='filer_video_image', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', help_text='preview image file', null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='filervideo',
            name='movie',
            field=filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.File', help_text='use .flv file or h264 encoded video file', null=True, verbose_name='movie file'),
        ),
    ]
