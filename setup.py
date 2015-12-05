#!/usr/bin/env python

from sys import platform
from platform import architecture

from setuptools import setup

from hilbert.information import __description__, __version__, __url_proj__ 

email=['kamel.derouiche@gmail.com']

with open('README') as file:
       long_description= file.read()

# Chek for Python 3
PY3 = sys.version_info[0] == 3

def install_data_files():
    """ """
    if sys.platform.startswith('netbsd'):
        """ """
        pass
    elif sys.platform.startswith('freebsd'):
        """ """
        pass
    elif sys.platform.startswith('linux'):
        if PY3:
            data_files = [('share/applications', ['script/hilbmetric.desktop']),
                          ('share/pixmaps', ['data/hilbmetric.png'])]
        else:
            data_files = [('share/applications', ['script/hilmetric.desktop'] ), 
                          ('share/pixmaps', ['data/hilbmetric.png'])]
    elif os.name =='nt':
            data_files = [('script', ['data/hilbmetric.ico'])]
    else:
        data_files = []
    return data_files
        
setup(
    name='hilbmetric',
    version=__version__,
    description=__description__,
    long_description=long_description,
    authors='HilbertMetric Developers',
    author_email=email,
    maintainer = 'HilbertMetric Developers',
    maintainer_email = email,
    url=__url_proj__,
    keywords=['hilbert, geometry', 'mesure', 'convex'],
    py_modules=['hilbmetric'],
    license='Apache-2.0',
    data_files=install_data_files(),
    install_requires=["sympy(>=0.7.6.1)", "PyQt4 (>=4.4)"],
    platforms='any',
    classifiers=[
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
    ],
)
