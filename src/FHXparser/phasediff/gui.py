import PySimpleGUI as sg
import webbrowser
import os.path

def selectfiles():
    flag = int()
    filter_frame = [
        [sg.Checkbox('Strip Whitespace', key='-WHITE-')],
        [sg.Checkbox('Strip Braces', key='-BRACE-')],
        [sg.Checkbox('Ignore Line Drawing', key='-LINE-')],
    ]
    layout = [
        [sg.Text('Select 2 FHX files to compare.')],
        [sg.Text('File 1'), sg.Input(disabled=True, expand_x=True), sg.FileBrowse(file_types=[('DeltaV Config Files','*.fhx')])],
        [sg.Text('File 2'), sg.Input(disabled=True, expand_x=True), sg.FileBrowse(file_types=[('DeltaV Config Files','*.fhx')])],
        [sg.Button('Show Filters', key='-EXPAND-'), sg.Submit('Compare'), sg.Cancel()],
        [sg.Frame('Filters', filter_frame, visible=False,key='-FILTERS-')]
        ]
    window = sg.Window('Phase Compare', layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"Cancel"):
            window.close()
            return None
        elif (event == 'Compare') and values[0] and values[1]:
            window.close()
            return values
        elif event == '-EXPAND-':
            if flag == 0:
                window['-FILTERS-'].update(visible=True)
                window['-EXPAND-'].update(text='Hide Filters')
                flag = 1
            elif flag == 1:    
                window['-FILTERS-'].update(visible=False)
                window['-EXPAND-'].update(text='Show Filters')
                flag = 0
                


def showhtml(filename):
    # lazy solution of letting browsers handle it
    webbrowser.open('file://' + os.path.realpath(filename))