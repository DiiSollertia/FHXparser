#!/usr/bin/env python
from . import selectfile
from . import handlehtml
from . import gui

def main():
    files = gui.selectfiles()
    if not files:
        return
    workdir = selectfile.getpath(files[0])
    html = handlehtml.makehtml(files)
    gui.showhtml(handlehtml.writehtml(html, workdir))

if __name__ == '__main__':
    main()
    input('Press ENTER to close.')