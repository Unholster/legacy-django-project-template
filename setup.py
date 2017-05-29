#!/usr/bin/env python
from setuptools import find_packages, setup

project_name = '{{project_name}}'

setup(
    name=project_name,
    version='0.2',
    packages=find_packages(),
    package_data={project_name: ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
