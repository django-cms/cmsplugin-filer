# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_video', '0002_auto_20160108_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filervideo',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_filer_video_filervideo', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
