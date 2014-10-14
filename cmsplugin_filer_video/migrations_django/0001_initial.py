# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import filer.fields.file
from cmsplugin_filer_video import settings


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerVideo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='cms.CMSPlugin', serialize=False)),
                ('movie_url', models.CharField(max_length=255, blank=True, null=True, verbose_name='movie url', help_text='vimeo or youtube video url. Example: http://www.youtube.com/watch?v=YFa59lK-kpo')),
                ('width', models.PositiveSmallIntegerField(verbose_name='width', default=settings.VIDEO_WIDTH)),
                ('height', models.PositiveSmallIntegerField(verbose_name='height', default=settings.VIDEO_HEIGHT)),
                ('auto_play', models.BooleanField(verbose_name='auto play', default=settings.VIDEO_AUTOPLAY)),
                ('auto_hide', models.BooleanField(verbose_name='auto hide', default=settings.VIDEO_AUTOHIDE)),
                ('fullscreen', models.BooleanField(verbose_name='fullscreen', default=settings.VIDEO_FULLSCREEN)),
                ('loop', models.BooleanField(verbose_name='loop', default=settings.VIDEO_LOOP)),
                ('bgcolor', models.CharField(default=settings.VIDEO_BG_COLOR, max_length=6, verbose_name='background color', help_text='Hexadecimal, eg ff00cc')),
                ('textcolor', models.CharField(default=settings.VIDEO_TEXT_COLOR, max_length=6, verbose_name='text color', help_text='Hexadecimal, eg ff00cc')),
                ('seekbarcolor', models.CharField(default=settings.VIDEO_SEEKBAR_COLOR, max_length=6, verbose_name='seekbar color', help_text='Hexadecimal, eg ff00cc')),
                ('seekbarbgcolor', models.CharField(default=settings.VIDEO_SEEKBARBG_COLOR, max_length=6, verbose_name='seekbar bg color', help_text='Hexadecimal, eg ff00cc')),
                ('loadingbarcolor', models.CharField(default=settings.VIDEO_LOADINGBAR_COLOR, max_length=6, verbose_name='loadingbar color', help_text='Hexadecimal, eg ff00cc')),
                ('buttonoutcolor', models.CharField(default=settings.VIDEO_BUTTON_OUT_COLOR, max_length=6, verbose_name='button out color', help_text='Hexadecimal, eg ff00cc')),
                ('buttonovercolor', models.CharField(default=settings.VIDEO_BUTTON_OVER_COLOR, max_length=6, verbose_name='button over color', help_text='Hexadecimal, eg ff00cc')),
                ('buttonhighlightcolor', models.CharField(default=settings.VIDEO_BUTTON_HIGHLIGHT_COLOR, max_length=6, verbose_name='button highlight color', help_text='Hexadecimal, eg ff00cc')),
                ('image', filer.fields.image.FilerImageField(null=True, to='filer.Image', help_text='preview image file', related_name='filer_video_image', blank=True, verbose_name='image')),
                ('movie', filer.fields.file.FilerFileField(null=True, to='filer.File', help_text='use .flv file or h264 encoded video file', blank=True, verbose_name='movie file')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
