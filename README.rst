cmsplugin-filer
===============

A set of cms plugins that replace the plugins shipped with django-cms with
versions that use file fields from django-filer.

Dependencies
------------

django-filer >= 0.8.0
django-cms >= 2.1
easy-thumbnails >= 1.0-alpha-13

Installation
------------

add the plugins to `INSTALLED_APPS`:

```
INSTALLED_APPS = (
    ...
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    ...
)
```

and then run `syncdb` or `migrate` if you're using South.