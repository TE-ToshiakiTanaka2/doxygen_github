#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" """
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

with open('requirements.in') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('requirements_dev.in') as requirements_dev_file:
    development_requirements = requirements_dev_file.read().splitlines()

test_requirements = ['pytest']

setup(
    name='doxygen_github',
    version='0.1.0',
    author='Toshiaki Tanaka',
    author_email='Your address email (eq. you@example.com)',
    license='MIT',
    url='https://github.com/TE-ToshiakiTanaka2/doxygen_github',
    description='A short description of the project',
    long_description=readme + '\n\n' + history,
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'doxygen_github = doxygen_github.cli:main',
        ],
    },
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
        'dev': development_requirements,
    },
)
