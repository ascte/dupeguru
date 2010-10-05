#!/usr/bin/env python3

import sys
import os
import os.path as op
import subprocess

def main():
    scriptpath = op.abspath(__file__)
    scriptfolder = op.dirname(scriptpath)
    newenv = {'PYTHONPATH': scriptfolder}
    subprocess.Popen([sys.executable, '-m', 'qt.{{edition}}.start'], env=newenv)

if __name__ == '__main__':
    sys.exit(main())