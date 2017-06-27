# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import django.db.models.deletion
import djangocms_attributes_field.fields
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerLink2Plugin',
            fields=[
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('url', models.CharField(max_length=2000, null=True, verbose_name='url', blank=True)),
                ('mailto', models.EmailField(help_text='An email address has priority over both pages and urls', max_length=254, null=True, verbose_name='mailto', blank=True)),
                ('link_style', models.CharField(default=' ', max_length=255, verbose_name='link style', choices=[(' ', 'Default')])),
                ('new_window', models.BooleanField(default=False, help_text='Do you want this link to open a new window?', verbose_name='new window?')),
                ('link_attributes', djangocms_attributes_field.fields.AttributesField(default=dict, help_text='Optional. Adds HTML attributes to the rendered link.', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cmsplugin_filer_link2_filerlink2plugin', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.File', null=True)),
                ('page_link', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', help_text='A link to a page has priority over urls.', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
