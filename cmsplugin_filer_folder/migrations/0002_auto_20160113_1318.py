# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.folder
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_folder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerfolder',
            name='folder',
            field=filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.SET_NULL, to='filer.Folder', null=True),
        ),
    ]
