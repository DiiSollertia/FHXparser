#!/usr/bin/env python
from . import selectfile
from . import handlehtml

def main():
    print('Select 2 phase FHX files.')
    file1 = selectfile.getfile()
    file2 = selectfile.getfile()
    workdir = selectfile.getpath(file1)
    html = handlehtml.makehtml(file1, file2)
    handlehtml.writehtml(html, workdir)


if __name__ == '__main__':
    main()
    input('Press ENTER to close.')