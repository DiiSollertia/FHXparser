#!/usr/bin/env python
from . import selectfile
from . import handlehtml
from . import gui
from .stripfhx import stripfhx

def main():
    mode, file1, file2 = gui.selectfiles()
    if mode in (None, 'Cancel'):
        return
    workdir = selectfile.getpath(file1)
    if mode == 'Strip FHX':
        stripfhx.stripfhx(file1, file2)
    html = handlehtml.makehtml(file1, file2)
    gui.showhtml(handlehtml.writehtml(html, workdir))

if __name__ == '__main__':
    main()
    input('Press ENTER to close.')