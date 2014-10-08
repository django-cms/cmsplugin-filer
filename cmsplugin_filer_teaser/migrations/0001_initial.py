# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import filer.fields.image
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerTeaser',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='cms.CMSPlugin', auto_created=True)),
                ('title', models.CharField(max_length=255, blank=True, verbose_name='title')),
                ('image_url', models.URLField(null=True, blank=True, default=None, verbose_name='alternative image url')),
                ('style', models.CharField(max_length=255, blank=True, default=settings.CMSPLUGIN_FILER_TEASER_DEFAULT_STYLE, choices=settings.CMSPLUGIN_FILER_TEASER_STYLE_CHOICES, verbose_name='Style')),
                ('use_autoscale', models.BooleanField(verbose_name='use automatic scaling', help_text='tries to auto scale the image based on the placeholder context', default=True)),
                ('width', models.PositiveIntegerField(null=True, blank=True, verbose_name='width')),
                ('height', models.PositiveIntegerField(null=True, blank=True, verbose_name='height')),
                ('free_link', models.CharField(null=True, help_text='if present image will be clickable', blank=True, verbose_name='link', max_length=255)),
                ('description', models.TextField(null=True, blank=True, verbose_name='description')),
                ('target_blank', models.BooleanField(verbose_name='open link in new window', default=False)),
                ('image', filer.fields.image.FilerImageField(null=True, verbose_name='image', to='filer.Image', blank=True)),
                ('page_link', cms.models.fields.PageField(null=True, verbose_name='page link', help_text='if present image will be clickable', to='cms.Page', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
