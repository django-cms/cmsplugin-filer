import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

dependency_links = [
    'http://github.com/pbs/django-cms/tarball/support/2.3.x#egg=django-cms-2.3.5pbs',
    'http://github.com/pbs/django-filer/tarball/master_pbs#egg=django-filer-0.9pbs',
]

setup(
    name = "cmsplugin-filer",
    version = "0.9.4pbs8",
    url = 'http://github.com/stefanfoulis/cmsplugin-filer',
    license = 'BSD',
    description = "django-cms plugins for django-filer",
    long_description = read('README.rst'),
    author = 'Stefan Foulis',
    author_email = 'stefan.foulis@gmail.com',
    packages = find_packages(),
    #package_dir = {'':'src'},
    dependency_links=dependency_links,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "django-cms>=2.3.5pbs, <2.3.6",
        "django-sekizai >= 0.4.2",
        "easy_thumbnails >= 1.0",
        "django-filer >= 0.9pbs, <0.9.1"
    ],
    include_package_data=True,
    zip_safe = False,
    setup_requires=['s3sourceuploader', ],
)
