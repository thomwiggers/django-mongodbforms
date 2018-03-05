#!/usr/bin/env python

import sys
from subprocess import check_call, CalledProcessError

from setuptools import setup


requirements = ['setuptools', 'mongoengine>=0.10.0']

if sys.version_info >= (3, 5):
    requirements.append('django')
else:
    requirements.append('django<2')


def convert_readme():
    try:
        check_call(["pandoc", "-f", "markdown_github", "-t",
                    "rst", "-o", "README.rst", "README.md"])
    except (OSError, CalledProcessError):
        return open('README.md').read()

    return open('README.rst').read()


setup(
    name='django-mongoengine-forms',
    version='0.4.5',
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
    install_requires=requirements,
    tests_require=['mongomock'],
    test_suite="tests.suite",
)
