# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='health-checker',
    version='0.0.1',
    description='health checker for MySQL database',
    long_description=readme,
    author='Mingxing LAI',
    author_email='me@mingxinglai',
    url='https://github.com/lalor/health-checker',
    packages=find_packages(exclude=('tests', 'docs'))
)

