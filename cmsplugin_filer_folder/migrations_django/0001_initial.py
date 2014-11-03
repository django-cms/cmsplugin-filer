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
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('style', models.CharField(default=settings.CMSPLUGIN_FILER_FOLDER_DEFAULT_STYLE, max_length=50, verbose_name='Style', choices=settings.CMSPLUGIN_FILER_FOLDER_STYLE_CHOICES)),
                ('folder', filer.fields.folder.FilerFolderField(to='filer.Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]