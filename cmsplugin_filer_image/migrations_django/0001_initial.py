# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import filer.fields.file
import filer.fields.image
from filer.settings import FILER_IMAGE_MODEL
import cms.models.fields

FILER_MODEL = FILER_IMAGE_MODEL or 'filer.Image'


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
        migrations.swappable_dependency(FILER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('style', models.CharField(max_length=50, verbose_name='Style', default=settings.CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE, blank=True, choices=settings.CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES)),
                ('caption_text', models.CharField(max_length=255, null=True, verbose_name='caption text', blank=True)),
                ('image_url', models.URLField(default=None, null=True, verbose_name='alternative image url', blank=True)),
                ('alt_text', models.CharField(max_length=255, null=True, verbose_name='alt text', blank=True)),
                ('use_original_image', models.BooleanField(default=False, help_text='do not resize the image. use the original image instead.', verbose_name='use the original image')),
                ('use_autoscale', models.BooleanField(default=False, help_text='tries to auto scale the image based on the placeholder context', verbose_name='use automatic scaling')),
                ('width', models.PositiveIntegerField(null=True, verbose_name='width', blank=True)),
                ('height', models.PositiveIntegerField(null=True, verbose_name='height', blank=True)),
                ('crop', models.BooleanField(default=True, verbose_name='crop')),
                ('upscale', models.BooleanField(default=True, verbose_name='upscale')),
                ('alignment', models.CharField(blank=True, max_length=10, null=True, verbose_name='image alignment', choices=[('left', 'left'), ('right', 'right')])),
                ('free_link', models.CharField(help_text='if present image will be clickable', max_length=255, null=True, verbose_name='link', blank=True)),
                ('original_link', models.BooleanField(default=False, help_text='if present image will be clickable', verbose_name='link original image')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('target_blank', models.BooleanField(default=False, verbose_name='Open link in new window')),
                ('file_link', filer.fields.file.FilerFileField(related_name='+', default=None, to='filer.File', blank=True, help_text='if present image will be clickable', null=True, verbose_name='file link')),
                ('image', filer.fields.image.FilerImageField(default=None, blank=True, to='filer.Image', null=True, verbose_name='image')),
                ('page_link', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='if present image will be clickable', null=True, verbose_name='page link')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('width', models.IntegerField(help_text='width in pixel.', verbose_name='width')),
                ('height', models.IntegerField(help_text='height in pixel.', verbose_name='height')),
                ('crop', models.BooleanField(default=True, verbose_name='crop')),
                ('upscale', models.BooleanField(default=True, verbose_name='upscale')),
            ],
            options={
                'ordering': ('width', 'height'),
                'verbose_name': 'thumbnail option',
                'verbose_name_plural': 'thumbnail options',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='filerimage',
            name='thumbnail_option',
            field=models.ForeignKey(blank=True, to='cmsplugin_filer_image.ThumbnailOption', help_text='overrides width, height, crop and upscale with values from the selected thumbnail option', null=True, verbose_name='thumbnail option'),
            preserve_default=True,
        ),
    ]
