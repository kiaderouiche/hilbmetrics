#!/usr/pkg/bin/env python
"""
Get information for hilbmetric
"""
from hilbert.common.__accessdata__ import install_data_files

__install_requires__ = [
    'sympy>= 1.0'
]

description = "Python program for the Hilbert projective metric"

__name__ = "hilbmetric"
__author__ = "K.I.A.Derouiche"
__descr__ = description
__platform__ = "NetBSD"
__data_file__ = install_data_files
__url__ = "https://github.com/kiaderouiche/hilbmetric"
__email__= "kamel.derouiche@gmail.com"
__keywords__= ['hilbert, geometry', 'mesure', 'convex']
__classifiers__= [
         'Development Status :: 3 - Alpha',
         'Environment :: Other Environment',
         'Intended Audience :: Education',
         'Intended Audience :: Developers',
         'Intended Audience :: Web',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: Apache',
         'Natural Language :: English',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3',
         'Topic :: Scientific/Engineering :: Mathematics',
         'Topic :: Scientific/Engineering :: Visualization',
]
