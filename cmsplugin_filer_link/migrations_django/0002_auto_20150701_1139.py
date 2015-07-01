# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='mailto',
            field=models.EmailField(help_text='An email address has priority over both pages and urls', max_length=75, null=True, verbose_name='email address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='url',
            field=models.CharField(max_length=2000, null=True, verbose_name='url', blank=True),
            preserve_default=True,
        ),
    ]
