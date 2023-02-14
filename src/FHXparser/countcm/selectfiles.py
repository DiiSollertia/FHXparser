import os.path
import sys
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilenames

def getfilepath(mode, attempt=5):
    root = tk.Tk()
    filelist = list()
    if mode == 1:
        # Folder mode
        print('Please select a folder containing FHX files.')
        workingpath = askdirectory(title='Select Folder')
        # Recursive if no files selected
        if checkempty(workingpath, attempt):
            workingpath, filelist = getfilepath(mode, attempt - 1)
        filelist = [(workingpath + '/' + filename) for filename in os.listdir(workingpath) if filename.endswith('.fhx')]
        if checkempty(filelist, attempt):
            workingpath, filelist = getfilepath(mode, attempt - 1)
    elif mode == 2:
        # Files mode
        print('Please select the FHX files.')
        filelist = askopenfilenames(title='Select FHX', filetypes=[('DeltaV Config Files','*.fhx')])
        # Recursive if no files selected
        if checkempty(filelist, attempt):
            workingpath, filelist = getfilepath(mode, attempt - 1)
        workingpath = os.path.dirname(filelist[0])
    root.withdraw()
    return workingpath, filelist

def checkempty(obj, attempt):
    # Recursive if no files selected
    if not obj:
        if attempt == 0:
            input('Exceeded retry limit. Press ENTER to exit.')
            sys.exit()
        print('Attempts left: ' + str(attempt))
        return True
    return False