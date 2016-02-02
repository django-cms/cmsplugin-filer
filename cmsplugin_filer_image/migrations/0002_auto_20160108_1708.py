# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerimage',
            name='file_link',
            field=filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, default=None, to='filer.File', blank=True, help_text='if present image will be clickable', null=True, verbose_name='file link'),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='filer.Image', null=True, verbose_name='image'),
        ),
    ]
