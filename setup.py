#!/usr/bin/env python

from setuptools import setup

with open('LICENSE') as file:
    __license__ = file.read()

__appinfo__ = {}
with open(os.path.join("hilbert", "common", "__appinfo__")) as fi:
    exec(f.read(), __appinfo__)

__data_files__ = __appinfo__.get('__data_file__', None)
include_dirs = __appinfo__.get('include_dirs', [])
ext_modules = __appinfo__.get('ext_modules', None)
install_requires = __appinfo__.get('install_requires', None)

setup(
    name=__appinfo__['__name__'],
    description=__appinfo__['__descr__'],
    long_descr=__appinfo__['__ldescr__'],
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