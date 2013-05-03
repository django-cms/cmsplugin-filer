import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-filer",
    version = "0.9.5a1.dev22",
    url = 'http://github.com/stefanfoulis/cmsplugin-filer',
    license = 'BSD',
    description = "django-cms plugins for django-filer",
    long_description = read('README.rst'),
    author = 'Stefan Foulis',
    author_email = 'stefan.foulis@gmail.com',
    packages = find_packages(),
    #package_dir = {'':'src'},
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
        "Django >= 1.3",
        "django-cms >= 2.2",
        "django-sekizai >= 0.4.2",
        "easy_thumbnails >= 1.0",
        "django-filer >= 0.9.5a1.dev2",
        # "https://github.com/stefanfoulis/django-filer/archive/feature/cmscloud-compat.tar.gz#egg=django-filer-0.9.5a1.dev2",
        # "https://divio:stionave@pkg.divio.ch/media/dists/django-filer-0.9.5a1.dev2.tar.gz#md5=3b2785b89af16bebe801e30bcf60151c#egg=django-filer",
    ],
    dependency_links = [
        "https://github.com/stefanfoulis/django-filer/archive/feature/cmscloud-compat/django-filer-0.9.5a1.dev2.tar.gz#egg=django-filer-0.9.5a1.dev2",
    ],
    include_package_data=True,
    zip_safe = False,
)
