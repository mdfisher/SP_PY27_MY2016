#!c:\Users\mdfisher\.virtualenvs\mayapy\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ipython==4.0.0-b1','console_scripts','ipython'
__requires__ = 'ipython==4.0.0-b1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('ipython==4.0.0-b1', 'console_scripts', 'ipython')()
    )
