import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-filer",
    version = "0.8.0",
    url = 'http://github.com/stefanfoulis/cmsplugin-filer',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "django-cms plugins for django-filer",
    long_description = read('README.rst'),
    author = 'Stefan Foulis',
    author_email = 'stefan.foulis@gmail.com',
    packages = find_packages(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
        'argparse',  # apparently needed by django-setuptest on python 2.6
    ),
    install_requires=[
        'Django>=1.3,<1.5',
        "django-cms>=2.2,<2.4",
        "django-sekizai>=0.4.2",
        "easy_thumbnails>=1.0",
        "django-filer>=0.9a1.dev1",
    ],
    include_package_data=True,
    zip_safe = False,
    dependency_links=[
        "https://github.com/stefanfoulis/django-filer/tarball/0.9a1.dev1#egg=django-filer-0.9a1.dev1",
    ],
)
