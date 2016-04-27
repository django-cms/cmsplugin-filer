# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0005_auto_20160224_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerimage',
            name='alignment',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='image alignment', choices=[('left', 'left'), ('right', 'right'), ('center', 'center')]),
        ),
    ]
