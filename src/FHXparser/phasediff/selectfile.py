import sys
import tkinter as tk
import os.path
from tkinter.filedialog import askopenfilename

def getfile(attempt=5):
    root = tk.Tk()
    # Single file mode
    print('Please select an FHX file.')
    f = askopenfilename(title='Select FHX', filetypes=[('DeltaV Config Files','*.fhx')])
    # Recursive if no file selected
    if checkempty(f, attempt):
        f = getfile(attempt - 1)
    root.withdraw()
    return f

def getpath(file):
    return os.path.dirname(file)

def checkempty(obj, attempt):
    # Recursive if no file selected
    if not obj:
        if attempt == 0:
            input('Exceeded retry limit. Press ENTER to exit.')
            sys.exit()
        print('Attempts left: ' + str(attempt))
        return True
    return False