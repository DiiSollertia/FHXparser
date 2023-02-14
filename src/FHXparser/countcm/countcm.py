#!/usr/bin/env python
#FHXparser.py
#V1.0.1

from . import selectfiles
from . import handlecsv
from . import parsefile
import sys

def main():
    try:
        mode = int(input('Enter:\n"1" to select a folder.\n"2" to select files.\n\nSelect mode:'))
    except:
        sys.exit()
    workingpath, fileList = selectfiles.getfilepath(mode)
    outputpath = handlecsv.writeheader(workingpath)
    moduleprefix = input('Enter module prefix to filter or simply press ENTER to continue.\n(Ex. "XV_", "EM_", "TIC_", etc. without quotation marks)\nFilter: ')
    moduleprefix = moduleprefix.upper()
    for fileName in fileList:
        print(parsefile.countmodconf(fileName, outputpath, moduleprefix))
    return 'Process completed.\nOutput generated in ' + outputpath

if __name__ == '__main__':
    main()
    input('Press ENTER to close.')