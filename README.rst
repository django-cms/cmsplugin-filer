===============
cmsplugin-filer
===============

A set of cms plugins that replace the plugins shipped with django-cms with
versions that use file fields from django-filer.

Dependencies
------------

* django-filer >= 0.9 (unrealeased: use develop branch from https://github.com/stefanfoulis/django-filer)
* Django >= 1.3
* django-cms >= 2.2
* django-sekizai >= 0.4.2
* easy_thumbnails >= 1.0

Installation
------------

add the plugins to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        'cmsplugin_filer_video',
        ...
    )

and then run ``syncdb`` or ``migrate`` if you're using South.

You can also set ``FILER_IMAGE_USE_ICON`` in your ``settings.py`` to configure ``cmsplugin_filer_image`` plugin to use 32x32 icons for representing plugin instances.

Upgrading
---------

Please note that current develop version moved plugin packages from `src` directory to project root.
This may break your installation if upgrading.
Uninstall any previous `cmsplugin_filer` installation (either from Pypi or from github repository) and reinstall it.