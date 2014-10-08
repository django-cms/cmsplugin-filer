# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerFolder',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title', null=True)),
                ('style', models.CharField(max_length=50, verbose_name='Style', default=settings.CMSPLUGIN_FILER_FOLDER_DEFAULT_STYLE, choices=settings.CMSPLUGIN_FILER_FOLDER_STYLE_CHOICES)),
                ('folder', filer.fields.folder.FilerFolderField(to='filer.Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
