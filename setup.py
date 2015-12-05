#!/usr/bin/env python

from setuptools import setup
from subprocess import call


def convert_readme():
    try:
        call(["pandoc", "-f", "markdown_github", "-t",
              "rst", "-o",  "README.txt", "readme.md"])
    except OSError:
        pass
    return open('README.txt').read()

setup(
    name='django-mongoengine-forms',
    version='0.4.0',
    description="An implementation of django forms using mongoengine.",
    author='Thom Wiggers',
    author_email='thom@thomwiggers.nl',
    packages=['mongodbforms'],
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
    zip_safe=False,
    install_requires=['setuptools', 'django>=1.9', 'mongoengine>=0.10.0'],
)
