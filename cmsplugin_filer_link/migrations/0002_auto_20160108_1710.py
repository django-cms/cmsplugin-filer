# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='file',
            field=filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.File', null=True),
        ),
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='page_link',
            field=cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', help_text='A link to a page has priority over urls.', null=True, verbose_name='page'),
        ),
    ]
