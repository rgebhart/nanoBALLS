"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    # to install, use:
    # pip install nanoballs
    
    # It will live on PyPI here: https://pypi.org/project/nanoballs/
    
    # The name of the project:
    name = 'nanoballs',
    
    # Version number:
    version = '1.0.2',
    
    # A one-line description or tagline of what your project does:
    description = 'A package for SEM image and particle analysis',
    
    # This should be a valid link to your project's main homepage:
    url = 'https://github.com/rgebhart/nanoBALLS',
    
    # Specify package directories or use find_packages()
    packages = find_packages()
)
