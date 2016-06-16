# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import filer.fields.image
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerTeaser',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='title', blank=True)),
                ('image_url', models.URLField(default=None, null=True, verbose_name='alternative image url', blank=True)),
                ('style', models.CharField(max_length=255, blank=True, default=settings.CMSPLUGIN_FILER_TEASER_DEFAULT_STYLE, choices=settings.CMSPLUGIN_FILER_TEASER_STYLE_CHOICES, verbose_name='Style')),
                ('use_autoscale', models.BooleanField(default=True, help_text='tries to auto scale the image based on the placeholder context', verbose_name='use automatic scaling')),
                ('width', models.PositiveIntegerField(null=True, verbose_name='width', blank=True)),
                ('height', models.PositiveIntegerField(null=True, verbose_name='height', blank=True)),
                ('free_link', models.CharField(help_text='if present image will be clickable', max_length=255, null=True, verbose_name='link', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('target_blank', models.BooleanField(default=False, verbose_name='open link in new window')),
                ('image', filer.fields.image.FilerImageField(verbose_name='image', blank=True, to='filer.Image', null=True)),
                ('page_link', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='if present image will be clickable', null=True, verbose_name='page link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
