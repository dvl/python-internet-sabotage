#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='internet-sabotage',
    version='0.1.2',
    description='Disable network connection for Testing',
    long_description=long_description,
    author='André Luiz',
    author_email='contato@xdvl.info',
    url='https://github.com/dvl/python-internet-sabotage',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing',
    ],
    keywords='internet disable unittest',
    packages=find_packages(),
    install_requires=[
        'contextdecorator',
    ],
    test_suite='tests',
)
