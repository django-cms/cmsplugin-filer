# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import cms.models.fields
from cmsplugin_filer_link.models import LINK_STYLES


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerLinkPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('url', models.CharField(max_length=255, null=True, verbose_name='url', blank=True)),
                ('mailto', models.EmailField(help_text='An email address has priority over both pages and urls', max_length=75, null=True, verbose_name='mailto', blank=True)),
                ('link_style', models.CharField(max_length=255, verbose_name='link style', default=LINK_STYLES[0][0], choices=LINK_STYLES)),
                ('new_window', models.BooleanField(default=False, help_text='Do you want this link to open a new window?', verbose_name='new window?')),
                ('file', filer.fields.file.FilerFileField(blank=True, to='filer.File', null=True)),
                ('page_link', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='A link to a page has priority over urls.', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
