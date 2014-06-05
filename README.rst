===============
cmsplugin-filer
===============

A set of cms plugins that replace the plugins shipped with django-cms with
versions that use file fields from django-filer.

Dependencies
============

* django-filer >= 0.9
* Django >= 1.4
* django-cms >= 2.2
* django-sekizai >= 0.4.2
* easy_thumbnails >= 1.0
* django-appconf

Installation
============

To get started using ``cmsplugin-filer``:

- install it with ``pip``::

    $ pip install cmsplugin-filer

- configure ``django-filer`` as documented in http://django-filer.readthedocs.org/en/latest/installation.html#configuration

- add the plugins to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        'cmsplugin_filer_video',
        ...
    )
    
- run ``syncdb`` or ``migrate`` if you're using South.

You can also set ``FILER_IMAGE_USE_ICON`` in your ``settings.py`` to configure ``cmsplugin_filer_image`` plugin to use 32x32 icons for representing plugin instances.

The default template in ``cmsplugin_filer_image`` expects the subject location functionality to be enabled.
Follow: http://django-filer.readthedocs.org/en/0.9.2/installation.html#subject-location-aware-cropping

Upgrading
=========

Please note that current develop version moved plugin packages from `src` directory to project root.
This may break your installation if upgrading.
Uninstall any previous `cmsplugin_filer` installation (either from Pypi or from github repository) and reinstall it.


Integrations
============


``djangocms-text-ckeditor``
---------------------------

``cmsplugin_filer_image`` provides integration with
`djangocms-text-ckeditor <http://pypi.python.org/pypi/djangocms-text-ckeditor/>`__.
Add this setting to enable it::

   TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

This allows dragging images into the text editor in Firefox and newer versions of IE.


Customisation
-------------

Most plugins (file, folder, image and teaser) support configuring custom "styles" (templates).

e.g add the following settings for the image plugin::

    CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
        ('default', 'Default'),
        ('boxed', 'Boxed'),
    )
    CMSPLUGIN_FILER_IMAGE_DEFAUL_STYLE = 'boxed'

Now, if a template exists at ``cmsplugin_filer_image/plugins/image/boxed.html`` it will be used. If not, it will fall
back to ``cmsplugin_filer_image/plugins/image/default.html``. If a css class in the default template is enough, it can
be used in the template as ``{{ instance.style }}``.

For backwards compatibility the plugin will always use ``cmsplugin_filer_image/image.html`` if it exists. Remove that
template after migrating to the new structure.
