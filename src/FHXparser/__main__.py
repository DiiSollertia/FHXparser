#!/usr/bin/env python
from countcm import countcm
from phasediff import phasediff

def main():
    submod = int(input('Enter 1 to parse Control Module FHX files.\nEnter 2 to compare two phase FHX files.\nMode: '))
    if submod == 1:
        countcm.main()
    elif submod == 2:
        phasediff.main()

if __name__ == '__main__':
    main()
    input('Press ENTER to close.')