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
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = (
        'Django>=1.2',
        'django-cms>=2.1',
        'django-filer>=0.8'
    ),
    include_package_data=True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
    ),
)
