#!/usr/bin/env python
from countcm import countcm
from phasediff import phasediff
import gui

def main():
    submod = str()
    while submod not in (None, 'Exit'):
        submod = gui.selectmode()
        if submod == 'Control Module Elements Counter':
            countcm.main()
        elif submod == 'Compare Phases':
            phasediff.main()

if __name__ == '__main__':
    main()