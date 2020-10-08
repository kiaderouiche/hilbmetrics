#!/usr/bin/env python3

import json
import os
from pathlib
import os.path

try:
    if os.environ.get('NO_SETUPTOOLS'):
        raise ImportError()
    from setuptools import setup, find_packages
    from setuptools.command import easy_install as easy_install_lib
    USE_SETUPTOOLS = 1
except ImportError:
    from distutils.core import setup
    USE_SETUPTOOLS = 0
easy_install_lib = None

wrkdir = Path('.')

lics = wrkdir /'LICENSE'
ldsc = wrkdir /'DESCR'
fvers = wrkdir /'version.json'

with lics.open() as milaf:
    __license__ = milaf.read()

with ldsc.open() as milaf:
    __ldescr__ = milaf.read()

with fvers.open() as milaf:
    __version__ = '.'.join(str(part) for part in json.load(milaf))

__appinfo__ = {}
contents = pathlib.Path("hilbert", "common", "__appinfo__.py")
exec(f.read_text(), __appinfo__)

__data_files__ = __appinfo__.get('__data_file__', None)
include_dirs = __appinfo__.get('include_dirs', [])
ext_modules = __appinfo__.get('ext_modules', None)
install_requires = __appinfo__.get('install_requires', None)

setup(
    name=__appinfo__['__name__'],
    description=__appinfo__['__descr__'],
    long_descr=__ldescr__,
    version=__version__,
    license=__license__,
    url=__appinfo__['__url__'],
    author=__appinfo__['__author__'],
    author_email=__appinfo__['__email__'],
    classifiers=__appinfo__['__classifiers__'],
    keywords=__appinfo__['__keywords__'],
    data_files=__data_files__,
    install_requires=__appinfo__['__install_requires__'],
    platforms=__appinfo__['__platform__'],
    ext_modules=ext_modules,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
