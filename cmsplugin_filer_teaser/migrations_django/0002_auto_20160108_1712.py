# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_teaser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerteaser',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='image', blank=True, to='filer.Image', null=True),
        ),
        migrations.AlterField(
            model_name='filerteaser',
            name='page_link',
            field=cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', help_text='if present image will be clickable', null=True, verbose_name='page link'),
        ),
    ]
