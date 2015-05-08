# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerlinkplugin',
            name='title',
            field=models.CharField(help_text='May be set to add information about the nature of a link.', max_length=255, null=True, verbose_name='name', blank=True),
            preserve_default=True,
        ),
    ]
