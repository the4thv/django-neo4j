from distutils.core import setup
from setuptools import find_packages
import os
import codecs
import re

LONG_DESCRIPTION = """
Use Neo4j as a backend database for your django project

Usage
-----
1. Install django-neo4j::  

      pip install django-neo4j  
      
2. Into settings.py file of your project, add::

      DATABASES = {
           'default': {
               'ENGINE': 'django-neo4j',
           }
       }
       
       
Requirements
------------  

1. Django-neo4j requires python 3.6 or above.  
2. Neo4j ?


How it works
------------  

stuff and things
"""


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
packages = find_packages()


def read(*parts):
    with codecs.open(os.path.join(BASE_DIR, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='djongo',
    version=find_version("django-neo4j", "__init__.py"),
    packages=packages,
    url='https://github.com/the4thv/django-neo4j/',
    license='AGPL',
    author='the4thv',
    author_email='the4thv@live.co.uk',
    description=(
        'Driver for allowing Django to use Neo4j as the database backend.'),
    install_requires=['django>=1.11'],
    long_description=LONG_DESCRIPTION,
    python_requires='>=3.6',
    keywords='Django MongoDB driver connector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
    ]
)
