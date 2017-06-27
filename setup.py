from setuptools import setup, find_packages

from cmsplugin_filer_link2 import __version__

setup(
    name="djangocms-link2",
    version=__version__,
    url='https://github.com/Blueshoe/djangocms-link2',
    license='BSD',
    description="django-cms link/-structure management plugin with filer file support",
    long_description=open('README.rst').read(),
    author='Michael Schilonka',
    author_email='michael@blueshoe.de',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.8",
        "django-filer >= 1.2.0",
        "django-cms >= 3.1",
        "djangocms-attributes-field",
        "requests"
    ],
    include_package_data=True,
    zip_safe=False,
)
