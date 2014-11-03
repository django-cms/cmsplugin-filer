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
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('target_blank', models.BooleanField(default=False, verbose_name='Open link in new window')),
                ('style', models.CharField(default=settings.CMSPLUGIN_FILER_FILE_DEFAULT_STYLE, choices=settings.CMSPLUGIN_FILER_FILE_STYLE_CHOICES, verbose_name='Style', blank=True, max_length=255)),
                ('file', filer.fields.file.FilerFileField(verbose_name='file', to='filer.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
