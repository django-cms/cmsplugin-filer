# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerlink2plugin',
            name='persistent_page_link',
            field=models.CharField(max_length=2000, null=True, verbose_name='internal url', blank=True),
        ),
    ]
