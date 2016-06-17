# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_link', '0002_auto_20160108_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerlinkplugin',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, help_text='Optional. Adds HTML attributes to the rendered link.'),
        ),
        migrations.AlterField(
            model_name='filerlinkplugin',
            name='mailto',
            field=models.EmailField(blank=True, help_text='An email address has priority over both pages and urls', max_length=254, null=True, verbose_name='mailto'),
        ),
    ]
