#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from tempfile import mkdtemp


HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        # filer configuration
        'easy_thumbnails',
        'mptt',
        'filer',
        'djangocms_text_ckeditor',
        # cmsplugin_filer configuration
        'cmsplugin_filer_folder',
        'cmsplugin_filer_link',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        'cmsplugin_filer_video',
    ],
    'LANGUAGE_CODE': 'en',
    'LANGUAGES': (
        ('en', 'English'),
        ('de', 'German'),
    ),
    'CMS_LANGUAGES': {
        1: [
            {
                'code': 'en',
                'name': 'English',
                'public': True,
            },
            {
                'code': 'de',
                'name': 'German',
                'public': True,
            },
        ],
        'default': {
            'hide_untranslated': False,
        },
    },
    'THUMBNAIL_PROCESSORS': (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    ),
    'FILE_UPLOAD_TEMP_DIR': mkdtemp(),
    'FILER_IMAGE_MODEL': False,
}
if os.environ.get('CUSTOM_IMAGE', False):
    HELPER_SETTINGS['FILER_IMAGE_MODEL'] = os.environ.get('CUSTOM_IMAGE', False)
    HELPER_SETTINGS['INSTALLED_APPS'].append('filer.test_utils.custom_image')


def run():
    from djangocms_helper import runner
    runner.cms('cmsplugin_filer_file')

if __name__ == "__main__":
    run()
