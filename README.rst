===============
djangocms-link2
===============

A link/-structure management plugin that replaces the plugin shipped with django-cms with a robust version that employs file fields from django-filer.
It can be used as a drop-in replacement for **cmsplugin_filer_link**. The package contains a management command to migrate
all existing Link-instances from cmsplugin_filer_link to **link2**.

.. image:: https://travis-ci.org/Blueshoe/djangocms-link2.svg?branch=master
    :target: https://travis-ci.org/Blueshoe/djangocms-link2
    :alt: Code Analysis

********
Features
********

cmsplugin_filer_link is already a great plugin and link2 builds on it. The following advantages are available in this package:

* robust django-cms link plugin which doesn't fail loudly
* persists the internal url as well
* can be copied safely between languages (even if the target page is not yet available in this language)
* internal and external links are monitored (through a management command)
* faulty links are visually highlighted for the content editor
* an admin page lists all faulty links
* easy migration from **cmsplugin_filer_link** (through a management command)

Dependencies
============

* django-filer >= 1.2
* Django >= 1.8
* django-cms >= 3.1
* djangocms-attributes-field
* requests

Installation
============


To get started using ``djangocms-link2``:

- install it with ``pip``::

    $ pip install djangocms-link2


- add the plugins to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'cmsplugin_filer_link2',
        ...
    )


- run ``migrate cmsplugin_filer_link2``.
- remove the default ``djangocms-link`` or ``cmsplugin_filer_link`` from your ``INSTALLED_APPS``
