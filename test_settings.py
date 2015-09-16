#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import six
from tempfile import mkdtemp


gettext = lambda s: s

HELPER_SETTINGS = {
    'NOSE_ARGS': [
        '-s',
    ],
    'ROOT_URLCONF': 'filer.test_utils.urls',
    'INSTALLED_APPS': [
        # filer configuration
        'easy_thumbnails',
        'mptt',
        'filer',
        # cmsplugin_filer configuration
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_link',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        'cmsplugin_filer_video',
    ],
    'LANGUAGE_CODE': 'en',
    'LANGUAGES': (
        ('en', gettext('English')),
        ('de', gettext('German')),
    ),
    'CMS_LANGUAGES': {
        1: [
            {
                'code': 'en',
                'name': gettext('English'),
                'public': True,
            },
            {
                'code': 'de',
                'name': gettext('German'),
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
    # FIXME: after new release of djangocms-link plugin remove it
    # FIXME: actually migrations should also be moved to a standard location
    # instead of current locations.
    'MIGRATION_MODULES': {
        'djangocms_link': 'djangocms_link.migrations_django',
        'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
        'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
        'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
        'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
        'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
        'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    },

}
if os.environ.get('CUSTOM_IMAGE', False):
    HELPER_SETTINGS['FILER_IMAGE_MODEL'] = os.environ.get('CUSTOM_IMAGE', False)
    HELPER_SETTINGS['INSTALLED_APPS'].append('filer.test_utils.custom_image')


def run(module_name='cmsplugin_filer_file'):
    from djangocms_helper import runner
    runner.cms(module_name)
    # runner.cms('cmsplugin_filer_link')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        run()
    option = (sys.argv[1] if isinstance(sys.argv[1], six.text_type)
              else six.u(sys.argv[1]))
    if option == '--plugin':
        sys.argv.pop(1)
        run(sys.argv.pop(1))
