# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_file', '0002_auto_20160112_1617'),
    ]

    operations = [
        migrations.RenameField('filerfile', 'file', 'source'),
    ]
