import PySimpleGUI as sg
import webbrowser
import os.path

def selectfiles():
    layout = [
        [sg.Text('Select 2 FHX files to compare.')],
        [sg.Text('File 1'), sg.Input(size=(60,1)), sg.FileBrowse(file_types=[('DeltaV Config Files','*.fhx')])],
        [sg.Text('File 2'), sg.Input(size=(60,1)), sg.FileBrowse(file_types=[('DeltaV Config Files','*.fhx')])],
        [sg.Submit('Strip FHX'), sg.Submit('Simple Compare'), sg.Cancel()],
        ]
    window = sg.Window('Phase Compare', layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"Cancel"):
            window.close()
            return event, None, None
        elif values[0] and values[1]:
            window.close()
            return event, values[0], values[1]

def showhtml(filename):
    # lazy solution of letting browsers handle it
    webbrowser.open('file://' + os.path.realpath(filename))