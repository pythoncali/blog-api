#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import blog-api
version = blog-api.__version__

setup(
    name='Blog API',
    version=version,
    author='',
    author_email='guillermo@guillermoalvarez.co',
    packages=[
        'blog-api',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['blog-api/manage.py'],
)
