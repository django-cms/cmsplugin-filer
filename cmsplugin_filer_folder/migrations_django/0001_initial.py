# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20141015_0046'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerFolder',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('style', models.CharField(default=b'list', max_length=50, verbose_name='Style', choices=[(b'list', 'List'), (b'slideshow', 'Slideshow')])),
                ('folder', filer.fields.folder.FilerFolderField(to='filer.Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
