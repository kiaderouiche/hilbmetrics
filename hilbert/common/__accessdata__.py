import os
import sys

# Chek for Python 3
PY3 = sys.version_info[0] == 3


def install_data_files():
    
    if sys.platform.startswith('netbsd'):
        
        pass
    elif sys.platform.startswith('freebsd'):
        
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
        dtfiles = []
    return datafiles