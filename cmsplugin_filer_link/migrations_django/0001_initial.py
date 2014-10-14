# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields
import filer.fields.file
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
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('url', models.CharField(max_length=255, verbose_name='url', blank=True, null=True)),
                ('mailto', models.EmailField(max_length=75, verbose_name='mailto', help_text='An email address has priority over both pages and urls', blank=True, null=True)),
                ('link_style', models.CharField(max_length=255, verbose_name='link style', default=LINK_STYLES[0][0], choices=LINK_STYLES)),
                ('new_window', models.BooleanField(verbose_name='new window?', help_text='Do you want this link to open a new window?', default=False)),
                ('file', filer.fields.file.FilerFileField(blank=True, to='filer.File', null=True)),
                ('page_link', cms.models.fields.PageField(verbose_name='page', help_text='A link to a page has priority over urls.', blank=True, to='cms.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
