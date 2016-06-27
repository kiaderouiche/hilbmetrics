#!/usr/pkg/bin/env python
"""
Get information for hilbmetric
"""
from __accessdata__.install_data_files import datafiles

__install_requires__ = [
    'sympy>= 1.0',
    'python-notify>=0.4.5',
]

description = "Python program for the Hilbert projective metric"

with open('README') as file:
       long_description = file.read()

__name__ = "hilbmetric"
__author__ = "K.I.A.Derouiche"
__descr__ = description
__ldescr__ = long_description
__version__ = "1.0-pre01"
__platform__ = "NetBSD"
__data_file__ = datafiles
__url__ = "https://github.com/kiaderouiche/hilbmetric"
__email__= "kamel.derouiche@gmail.com"
__keywords__= ['hilbert, geometry', 'mesure', 'convex']
__classifiers__= [
         'Development Status :: 3 - Alpha',
         'Environment :: Other Environment',
         'Intended Audience :: Education',
         'Intended Audience :: Developers',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: Apache',
         'Natural Language :: English',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3',
         'Topic :: Scientific/Engineering :: Mathematics',
         'Topic :: Scientific/Engineering :: Visualization',
]