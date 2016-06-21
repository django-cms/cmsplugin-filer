===============
cmsplugin-filer
===============

A set of cms plugins that replace the plugins shipped with django-cms with
versions that use file fields from django-filer.

Warning: ::

    Starting with version 1.1.0, support for Python 2.6, Django 1.7 or lower
    and django CMS 3.0.x and lower was dropped. Please pin your dependencies
    to ``cmsplugin-filer<1.1.0`` for older projects.

    Starting with version 0.10 support for django CMS 2.x was dropped
    (table renaming magic removal). Pin your dependencies to
    ``cmsplugin-filer<0.10`` for django-cms 2.x projects.


Dependencies
============

* django-filer >= 1.2
* Django >= 1.8
* django-cms >= 3.1
* django-sekizai >= 0.4.2
* easy_thumbnails >= 1.0
* django-appconf
* djangocms-attributes-field


Installation
============

To get started using ``cmsplugin-filer``:

- install it with ``pip``::

    $ pip install cmsplugin-filer

- configure ``django-filer`` as documented in https://django-filer.readthedocs.io/en/latest/installation.html#configuration

- add the plugins to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_link',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        'cmsplugin_filer_video',
        ...
    )


- run ``migrate``.

You can also set ``FILER_IMAGE_USE_ICON`` in your ``settings.py`` to configure
``cmsplugin_filer_image`` plugin to use 32x32 icons for representing
plugin instances.

The default template in ``cmsplugin_filer_image`` expects the subject location functionality to be enabled.
Follow: https://django-filer.readthedocs.io/en/latest/installation.html#subject-location-aware-cropping

Upgrading to version 1.1
========================

In version 1.1 there are two backward incompatible changes:

Migrations layout
-----------------

Migrations have been moved back to the standard location. cmsplugin_filer related
``MIGRATION_MODULE`` setting items **must** be removed for cmsplugin_filer 1.1 to work

Removal of ``ThumbnailOption`` model
------------------------------------
``ThumbnailOption`` has been moved to ``filer`` (since filer 1.2).
You **must** update your models and migrations referencing ``ThumbnailOption`` for this to work.

Upgrade process involves updating your models and migrations.

model.py
^^^^^^^^

Add::

    try:
        from filer.models import ThumbnailOption
        thumbnail_model = 'filer.ThumbnailOption'
    except ImportError:
        from cmsplugin_filer_image.models import ThumbnailOption
        thumbnail_model = 'cmsplugin_filer_image.ThumbnailOption'

If you use the string syntax (e.g.: ``thumb_field = models.ForeignKey('cmsplugin_filer_image.ThumbnailOption')``)
use ``thumbnail_model`` string as defined above (e.g.: ``thumb_field = models.ForeignKey(thumbnail_model)``
If using the model directly you don't have to change the fields definition

Django 1.7+ migrations
^^^^^^^^^^^^^^^^^^^^^^

For every migration file that references ``ThumbnailOption`` add the following import::

    from myapp.models import thumbnail_model

and change all ``'cmsplugin_filer_image.ThumbnailOption'`` to ``thumbnail_model``

South migrations
^^^^^^^^^^^^^^^^

In every migration file add the following import::

    from myapp.models import thumbnail_model

and change all ``'cmsplugin_filer_image.ThumbnailOption'`` to ``thumbnail_model`` and
``u"orm['cmsplugin_filer_image.ThumbnailOption']"`` to ``u"orm['%s']" % thumbnail_model``.


The default template in ``cmsplugin_filer_image`` expects the subject location
functionality to be enabled.
Follow: http://django-filer.readthedocs.org/en/0.9.2/installation.html#subject-location-aware-cropping

Please note that current develop version moved plugin packages from `src`
directory to project root. This may break your installation if upgrading.
Uninstall any previous `cmsplugin_filer` installation (either from PyPI or
from github repository) and reinstall it.


Integrations
============


``djangocms-text-ckeditor``
---------------------------

``cmsplugin_filer_image`` provides integration with
`djangocms-text-ckeditor <http://pypi.python.org/pypi/djangocms-text-ckeditor/>`__.
Add this setting to enable it::

    TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

This allows dragging images into the text editor in Firefox and newer versions
of IE.


Customisation
-------------

Most plugins (file, folder, image and teaser) support configuring custom
"styles" (templates).

e.g add the following settings for the image plugin::

    CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
        ('default', 'Default'),
        ('boxed', 'Boxed'),
    )
    CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE = 'boxed'

Now, if a template exists at ``cmsplugin_filer_image/plugins/image/boxed.html``
it will be used. If not, it will fall back to ``cmsplugin_filer_image/plugins/image/default.html``.
If a css class in the default template is enough, it can be used in the
template as ``{{ instance.style }}``.

For backwards compatibility the plugin will always use ``cmsplugin_filer_image/image.html`` if it exists. Remove that
template after migrating to the new structure.


Classes
-------

Classes like ``left``, ``center``, ``right`` and ``img-responsive`` are given by the plugin to use in your own projects.
