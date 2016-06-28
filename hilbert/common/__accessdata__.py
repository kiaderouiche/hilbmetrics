import os
import sys

# Chek for Python 3
PY3 = sys.version_info[0] == 3


def install_data_files():
    if sys.platform.startswith('netbsd'):
        data_files = [('/usr/pkg/share/applications', ['script/hilbmetric.desktop']),
                          ('/usr/pkg/share/pixmaps', ['data/hilbmetric.png'])]
    elif sys.platform.startswith('freebsd'):
        data_files = [('/usr/local/share/applications', ['script/hilbmetric.desktop']),
                          ('/usr/local/share/pixmaps', ['data/hilbmetric.png'])]
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