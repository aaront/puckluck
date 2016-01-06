#!/usr/bin/env python

import re
import ast

from codecs import open

from setuptools import setup, find_packages

requires = []

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('puckluck/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='puckluck',
    version=version,
    description='A simple web interface for (intermediate?) NHL stats & charts',
    long_description=open('README.rst', 'r', 'utf-8').read(),
    author='Aaron Toth',
    author_email='ajtoth@acm.org',
    url='http://github.com/aaront/puckluck',
    include_package_data=True,
    packages=find_packages(),
    install_requires=requires,
    package_data={'': ['LICENSE']},
    package_dir={'puckluck': 'puckluck'},
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    )
)
