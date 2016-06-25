# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def move_thumbnail_opt_to_filer(apps, schema_editor):
    ThumbnailOption = apps.get_model('cmsplugin_filer_image', 'ThumbnailOption')
    ThumbnailOptionNew = apps.get_model('filer', 'ThumbnailOption')
    for obj in ThumbnailOption.objects.all():
        try:
            ThumbnailOptionNew.objects.get(
                name=obj.name,
                width=obj.width,
                height=obj.height,
                crop=obj.crop,
                upscale=obj.upscale
            )
        except ThumbnailOptionNew.DoesNotExist:
            th = ThumbnailOptionNew(
                id=obj.id,
                name=obj.name,
                width=obj.width,
                height=obj.height,
                crop=obj.crop,
                upscale=obj.upscale
            )
            th.save()

def move_thumbnail_opt_to_cms(apps, schema_editor):
    ThumbnailOption = apps.get_model('filer', 'ThumbnailOption')
    ThumbnailOptionOld = apps.get_model('cmsplugin_filer_image', 'ThumbnailOption')
    for obj in ThumbnailOption.objects.all():
        try:
            ThumbnailOptionOld.objects.get(
                name=obj.name,
                width=obj.width,
                height=obj.height,
                crop=obj.crop,
                upscale=obj.upscale
            )
        except ThumbnailOptionOld.DoesNotExist:
            th = ThumbnailOptionOld(
                id=obj.id,
                name=obj.name,
                width=obj.width,
                height=obj.height,
                crop=obj.crop,
                upscale=obj.upscale
            )
            th.save()
 

class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0002_auto_20160108_1708'),
        ('filer', '0003_thumbnailoption'),
    ]

    operations = [
        migrations.RunPython(move_thumbnail_opt_to_filer, move_thumbnail_opt_to_cms),
    ]
