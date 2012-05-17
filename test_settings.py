#-*- coding: utf-8 -*-
import os
DEBUG = True
PACKAGE_ROOT = os.path.abspath( os.path.dirname(__file__) )
TMP_ROOT = os.path.abspath( os.path.join(PACKAGE_ROOT, "tmp") )
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(TMP_ROOT,"filer_test.sqlite3"),
        },
    }
INSTALLED_APPS = [
    "filer",
    "cms",
    "menus",
    "sekizai",
    "mptt",
    "easy_thumbnails",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.staticfiles",

    "cmsplugin_filer_file",
    "cmsplugin_filer_folder",
    "cmsplugin_filer_image",
    "cmsplugin_filer_teaser",
    "cmsplugin_filer_video",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages"
]
CMS_TEMPLATES = []

ROOT_URLCONF = "test_urls"

MEDIA_ROOT = os.path.abspath( os.path.join(TMP_ROOT, "media") )
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
