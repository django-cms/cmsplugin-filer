import os
from setuptools import setup
from filer_cmsplugins import __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-filer-cmsplugins",
    version = __version__,
    url = 'http://github.com/stefanfoulis/django-filer-cmsplugins',
    license = 'BSD',
    description = "django-cms plugins for django-filer",
    long_description = read('README'),
    author = 'Stefan Foulis',
    author_email = 'stefan.foulis@gmail.com',
    packages = ('filer_cmsplugins',),
    #package_dir = {'': 'src'},
    install_requires = ['setuptools','django','django-cms',],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)