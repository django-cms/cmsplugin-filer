# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20141015_0046'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerVideo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('movie_url', models.CharField(help_text='vimeo or youtube video url. Example: http://www.youtube.com/watch?v=YFa59lK-kpo', max_length=255, null=True, verbose_name='movie url', blank=True)),
                ('width', models.PositiveSmallIntegerField(default=320, verbose_name='width')),
                ('height', models.PositiveSmallIntegerField(default=240, verbose_name='height')),
                ('auto_play', models.BooleanField(default=False, verbose_name='auto play')),
                ('auto_hide', models.BooleanField(default=False, verbose_name='auto hide')),
                ('fullscreen', models.BooleanField(default=True, verbose_name='fullscreen')),
                ('loop', models.BooleanField(default=False, verbose_name='loop')),
                ('bgcolor', models.CharField(default=b'000000', help_text='Hexadecimal, eg ff00cc', max_length=6, verbose_name='background color')),
                ('textcolor', models.CharField(default=b'FFFFFF', help_text='Hexadecimal, eg ff00cc', max_length=6, verbose_name='text color')),
                ('seekbarcolor', models.CharField(default=b'13ABEC', help_text='Hexadecimal, eg ff00cc', max_length=6, verbose_name='seekbar color')),
                ('seekbarbgcolor', models.CharField(default=b'333333', help_text='Hexadecimal, eg ff00cc', max_length=6, verbose_name='seekbar bg color')),
                ('loadingbarcolor', models.CharField(default=b'828282', help_text='Hexadecimal, eg ff00cc', max_length=6, verbose_name='loadingbar color')),
                ('buttonoutcolor', models.CharField(default=b'333333', help_text='Hexadecimal, eg ff00cc', max_length=6, verbose_name='button out color')),
                ('buttonovercolor', models.CharField(default=b'000000', help_text='Hexadecimal, eg ff00cc', max_length=6, verbose_name='button over color')),
                ('buttonhighlightcolor', models.CharField(default=b'FFFFFF', help_text='Hexadecimal, eg ff00cc', max_length=6, verbose_name='button highlight color')),
                ('image', filer.fields.image.FilerImageField(related_name='filer_video_image', blank=True, to='filer.Image', help_text='preview image file', null=True, verbose_name='image')),
                ('movie', filer.fields.file.FilerFileField(blank=True, to='filer.File', help_text='use .flv file or h264 encoded video file', null=True, verbose_name='movie file')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
