#!/usr/bin/env python

from setuptools import setup
from subprocess import call


def convert_readme():
    try:
        call(["pandoc", "-f", "markdown_github", "-t",
              "rst", "-o",  "README.rst", "README.md"])
    except OSError:
        return open('README.md').read()

    return open('README.rst').read()

setup(
    name='django-mongoengine-forms',
    version='0.4.0',
    description="An implementation of django forms using mongoengine.",
    author='Thom Wiggers',
    author_email='thom@thomwiggers.nl',
    packages=['mongodbforms', 'tests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    license='New BSD License',
    long_description=convert_readme(),
    include_package_data=True,
    provides=['mongodbforms'],
    obsoletes=['mongodbforms'],
    url='https://github.com/thomwiggers/django-mongoengine-forms/',
    zip_safe=False,
    install_requires=['setuptools', 'django>=1.9', 'mongoengine>=0.10.0'],
    test_suite="tests",
)
