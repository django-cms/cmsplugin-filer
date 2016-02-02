# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerfile',
            name='file',
            field=filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='file', to='filer.File', null=True),
        ),
    ]
