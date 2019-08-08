#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from os.path import join

from setuptools import (
    setup,
    find_packages,
)

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()

install_requirements = [
    'starfish-py==0.5.0',
]

setup_requirements = ['pytest-runner', ]

test_requirements = [
    'codacy-coverage',
    'coverage',
    'docker',
    'flake8',
    'mccabe',
    'pyflakes',
    'pytest',
    'tox',
]

# Possibly required by developers of starfish-py:
dev_requirements = [
    'bumpversion',
    'pkginfo',
    'twine',
    'watchdog',
]

setup(
    author="dex-company",
    author_email='devops@dex.sg',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Oceanprotocol/Dex  - File Transfer: Ocean DropBox",
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements + test_requirements,
    },
    scripts=['cli/ocean_drop'],
    data_files=['cli/ocean_drop_local.conf', 'cli/ocean_drop_nile.conf'],
    install_requires=install_requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='ocean_drop',
    name='ocean_drop',
    packages=find_packages(),
#    packages=packages,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com//DEX-Company/ocean-drop',
    version='0.0.1',
    zip_safe=False,
)
