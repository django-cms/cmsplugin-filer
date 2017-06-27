# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link2', '0003_linkhealthstate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerlink2plugin',
            name='url',
            field=models.CharField(help_text='The url must specify the protocol, e.g. https://DOMAIN', max_length=2000, null=True, verbose_name='url', blank=True),
        ),
        migrations.AlterField(
            model_name='linkhealthstate',
            name='state',
            field=models.CharField(max_length=3, choices=[('3xx', 'Redirected'), ('4xx', 'Not reachable'), ('5xx', 'Server error'), ('bad', 'Bad configured')]),
        ),
    ]
