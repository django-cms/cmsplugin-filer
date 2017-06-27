# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link2', '0004_auto_20170306_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linkhealthstate',
            options={'verbose_name': 'Link Health State', 'verbose_name_plural': 'Link Health States'},
        ),
        migrations.AlterField(
            model_name='linkhealthstate',
            name='detected',
            field=models.DateTimeField(help_text='Date and time when the faulty link state was detected.', verbose_name='Detected on', auto_now=True),
        ),
        migrations.AlterField(
            model_name='linkhealthstate',
            name='link',
            field=models.OneToOneField(related_name='linkhealth', verbose_name='Link', to='cmsplugin_filer_link2.FilerLink2Plugin'),
        ),
        migrations.AlterField(
            model_name='linkhealthstate',
            name='state',
            field=models.CharField(max_length=3, verbose_name='State', choices=[('3xx', 'Redirected'), ('4xx', 'Not reachable'), ('5xx', 'Server error'), ('bad', 'Bad configured')]),
        ),
    ]
