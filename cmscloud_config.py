# -*- coding: utf-8 -*-
from cmscloud_client import forms


class Form(forms.BaseForm):
    """
    django-filer and cmsplugin-filer settings
    """
    # enable_debug = forms.CheckboxField('enable debug mode')
    # enable_file_plugin = forms.CheckboxField('enable file plugin')
    # enable_image_plugin = forms.CheckboxField('enable image plugin')
    # enable_folder_plugin = forms.CheckboxField('enable folder plugin')
    # enable_link_plugin = forms.CheckboxField('enable link plugin')
    # enable_teaser_plugin = forms.CheckboxField('enable teaser plugin')
    # enable_video_plugin = forms.CheckboxField('enable video plugin')


    def to_settings(self, data, settings):
        # THUMBNAIL_PROCESSORS = list(settings.get('THUMBNAIL_PROCESSORS', DEFAULT_THUMBNAIL_PROCESSORS))
        # if 'filer.thumbnail_processors.scale_and_crop_with_subject_location' not in THUMBNAIL_PROCESSORS:
        #     THUMBNAIL_PROCESSORS.append('filer.thumbnail_processors.scale_and_crop_with_subject_location')
        # settings['THUMBNAIL_PROCESSORS'] = THUMBNAIL_PROCESSORS

        settings['THUMBNAIL_PROCESSORS'] = (
            'easy_thumbnails.processors.colorspace',
            'easy_thumbnails.processors.autocrop',
            'filer.thumbnail_processors.scale_and_crop_with_subject_location',
            'easy_thumbnails.processors.filters',
        )
        settings['THUMBNAIL_SOURCE_GENERATORS'] = (
                 'easy_thumbnails.source_generators.pil_image',
        )
        # settings['FILER_DEBUG'] = data['enable_debug']
        # settings['DEBUG'] = data['enable_debug']
        # settings['TEMPLATE_DEBUG'] = data['enable_debug']

        # INSTALLED_APPS = settings['INSTALLED_APPS']
        #
        # for key, value in data.items():
        #     if not key.startswith('enable_') or not key.endswith('_plugin'):
        #         continue
        #     if not value:
        #         continue
        #     plugin_name = key[7:-7]
        #     INSTALLED_APPS.append('cmsplugin_filer_%s' % plugin_name)
        return settings
