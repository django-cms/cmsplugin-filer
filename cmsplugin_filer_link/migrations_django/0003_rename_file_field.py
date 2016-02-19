# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0002_auto_20160108_1710'),
    ]

    operations = [
        migrations.RenameField('filerlinkplugin', 'file', 'source')
    ]
