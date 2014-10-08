# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import filer.fields.file
import cms.models.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='cms.CMSPlugin', primary_key=True, serialize=False)),
                ('style', models.CharField(max_length=50, verbose_name='Style', default=settings.CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE, blank=True, choices=settings.CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES)),
                ('caption_text', models.CharField(max_length=255, null=True, verbose_name='caption text', blank=True)),
                ('image_url', models.URLField(null=True, verbose_name='alternative image url', default=None, blank=True)),
                ('alt_text', models.CharField(max_length=255, null=True, verbose_name='alt text', blank=True)),
                ('use_original_image', models.BooleanField(help_text='do not resize the image. use the original image instead.', verbose_name='use the original image', default=False)),
                ('use_autoscale', models.BooleanField(help_text='tries to auto scale the image based on the placeholder context', verbose_name='use automatic scaling', default=False)),
                ('width', models.PositiveIntegerField(null=True, verbose_name='width', blank=True)),
                ('height', models.PositiveIntegerField(null=True, verbose_name='height', blank=True)),
                ('crop', models.BooleanField(verbose_name='crop', default=True)),
                ('upscale', models.BooleanField(verbose_name='upscale', default=True)),
                ('alignment', models.CharField(max_length=10, null=True, choices=[('left', 'left'), ('right', 'right')], verbose_name='image alignment', blank=True)),
                ('free_link', models.CharField(max_length=255, null=True, verbose_name='link', help_text='if present image will be clickable', blank=True)),
                ('original_link', models.BooleanField(help_text='if present image will be clickable', verbose_name='link original image', default=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('target_blank', models.BooleanField(verbose_name='Open link in new window', default=False)),
                ('file_link', filer.fields.file.FilerFileField(blank=True, related_name='+', help_text='if present image will be clickable', null=True, verbose_name='file link', default=None, to='filer.File')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, verbose_name='image', default=None, to='filer.Image')),
                ('page_link', cms.models.fields.PageField(blank=True, help_text='if present image will be clickable', null=True, verbose_name='page link', to='cms.Page')),
            ],
            options={
                'verbose_name': 'filer image',
                'verbose_name_plural': 'filer images',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ThumbnailOption',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('width', models.IntegerField(help_text='width in pixel.', verbose_name='width')),
                ('height', models.IntegerField(help_text='height in pixel.', verbose_name='height')),
                ('crop', models.BooleanField(verbose_name='crop', default=True)),
                ('upscale', models.BooleanField(verbose_name='upscale', default=True)),
            ],
            options={
                'verbose_name': 'thumbnail option',
                'ordering': ('width', 'height'),
                'verbose_name_plural': 'thumbnail options',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='filerimage',
            name='thumbnail_option',
            field=models.ForeignKey(blank=True, help_text='overrides width, height, crop and upscale with values from the selected thumbnail option', null=True, verbose_name='thumbnail option', to='cmsplugin_filer_image.ThumbnailOption'),
            preserve_default=True,
        ),
    ]
