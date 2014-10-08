# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerFile',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, to='cms.CMSPlugin', primary_key=True)),
                ('title', models.CharField(null=True, verbose_name='title', blank=True, max_length=255)),
                ('target_blank', models.BooleanField(verbose_name='Open link in new window', default=False)),
                ('style', models.CharField(default=settings.CMSPLUGIN_FILER_FILE_DEFAULT_STYLE, choices=settings.CMSPLUGIN_FILER_FILE_STYLE_CHOICES, verbose_name='Style', blank=True, max_length=255)),
                ('file', filer.fields.file.FilerFileField(to='filer.File', verbose_name='file')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
