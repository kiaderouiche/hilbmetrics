#!/usr/bin/env python

from setuptools import setup

__appinfo__ = {}
with open(os.path.join("hilbert", "common", "__appinfo__")) as fi:
    exec(f.read(), __appinfo__)

data_files = __appinfo__.get('data_files', None)
include_dirs = __appinfo__.get('include_dirs', [])
ext_modules = __appinfo__.get('ext_modules', None)
install_requires = __appinfo__.get('install_requires', None)

setup(
    name=__appinfo__['__name__'],
    description=__appinfo__['__descr__'],
    long_descr=__appinfo__['__ldescr__'],
    version=__version__,
    license=__appinfo__['__license__'],
    url=__appinfo__['__url__'],
    author=__appinfo__['__author__'],
    author_email=__appinfo__['__email__'],
    classifiers=__appinfo__['__classifiers__'],
    keywords=__appinfo__['__keywords__'],
    data_files=data_files,
    install_requires=__appinfo__['__install_requires__'],
    platforms=__appinfo__['__platform__'],
    ext_modules=ext_modules,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

# setup(
#     name='hilbmetric',
#     version=__version__,
#     description=__description__,
#     long_description=long_description,
#     authors='HilbertMetric Developers',
#     author_email=__email__,
#     maintainer = 'HilbertMetric Developers',
#     maintainer_email =__email__,
#     url=__url_proj__,
#     
#     py_modules=['hilbmetric'],
#     license='Apache-2.0',
#     data_files=install_data_files(),
#     install_requires=["sympy(>=0.7.6.1)", "PyQt4 (>=4.4)"],
#     platforms='any',
# )
