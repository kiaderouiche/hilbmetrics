#!/usr/pkg/bin/env python
"""
Get information for hilbmetric
"""
from hilbert.common.__accessdata__ import install_data_files

__install_requires__ = [
    #'PyQt5',
    'sympy>= 1.6.2',
    #'opencv-python>= 3.4',
    #'scipy>= 1.0.0',
]

description = "Python program for the Hilbert projective metric"

__name__ = "hilbmetric"
__author__ = "K.I.A.Derouiche"
__descr__ = description
__platform__ = "any"
__data_file__ = install_data_files
__url__ = "https://github.com/kiaderouiche/hilbmetric"
__email__= "kamel.derouiche@gmail.com"
__keywords__= ['hilbert, geometry', 'mesure', 'convex', 'manifold', 'hyperbolic', 'birapport', 'ln', 'hull']
__classifiers__= [
         'Development Status :: 3 - Alpha',
         'Environment :: Other Environment',
         'Intended Audience :: Education',
         'Intended Audience :: Developers',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: Apache',
         'Natural Language :: English',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 3',
         'Topic :: Scientific/Engineering :: Mathematics',
         'Topic :: Scientific/Engineering :: Visualization',
]
