#!c:\Users\mdfisher\.virtualenvs\mayapy\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pymel==1.0.0','console_scripts','ipymel'
__requires__ = 'pymel==1.0.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pymel==1.0.0', 'console_scripts', 'ipymel')()
    )
