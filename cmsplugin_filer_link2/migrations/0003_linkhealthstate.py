# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link2', '0002_filerlink2plugin_persistent_page_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkHealthState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=3, choices=[('3xx', 'Redirected'), ('4xx', 'Not reachable'), ('5xx', 'Server error')])),
                ('detected', models.DateTimeField(auto_now=True)),
                ('link', models.OneToOneField(related_name='linkhealth', to='cmsplugin_filer_link2.FilerLink2Plugin')),
            ],
        ),
    ]
