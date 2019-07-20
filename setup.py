#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Abhishek Parmar",
    author_email='abhishek.parmar@somaiya.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Detect phishing websites using machine learning",
    entry_points={
        'console_scripts': [
            'phishing_detection=phishing_detection.cli:main',
        ],
    },
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    data_files=[('',['phishing_detection/data/model.sav'])],
    keywords='phishing_detection',
    name='phishing_detection',
    packages=find_packages(include=['phishing_detection']),
    package_data={'phishing_detection':['data/*.sav']},
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/abhi-parmar/phishing_detection',
    version='0.1',
    install_requires=[
        'pysafebrowsing'
    ],
    zip_safe=False,
)
