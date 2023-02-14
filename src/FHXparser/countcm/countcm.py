#!/usr/bin/env python
#FHXparser.py
#V1.0.1

from . import handlecsv
from . import gui
import os

def main():
    filelist = gui.selectfiles()
    if not filelist:
        return
    print(filelist)
    print(filelist[0])
    workdir = os.path.dirname(filelist[0])
    print(workdir)
    outputpath = handlecsv.writeheader(workdir)
    moduleprefix = gui.selectprefix()
    gui.loadingbar(filelist, outputpath, moduleprefix)
    gui.success(outputpath)

if __name__ == '__main__':
    main()