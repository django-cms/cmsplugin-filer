# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_teaser', '0002_auto_20160108_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerteaser',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_filer_teaser_filerteaser', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
