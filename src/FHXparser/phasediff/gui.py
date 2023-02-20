import PySimpleGUI as sg
import webbrowser
import os.path

def selectfiles():
    flag = int()
    filter_frame = [
        [sg.Text('Strip: '), sg.Checkbox('Whitespace', key='-WHITE-'),sg.Checkbox('Braces', key='-BRACE-')],
        [sg.Text('Ignore: '),sg.Checkbox('Line Drawing', key='-LINE-'),sg.Checkbox('User Comments', key='-COMMENT-'),sg.Checkbox('Embedded Composite Names', key='-EC-')],
        [sg.Text('No. of Context Lines:'), sg.Input('0', enable_events=True, key='-CONTEXT-')]
    ]
    layout = [
        [sg.Text('Select 2 FHX/CSV files to compare.')],
        [sg.Text('File 1'), sg.Input(disabled=True, size=(80,1), expand_x=True), sg.FileBrowse(file_types=(('DeltaV Config Files','*.fhx'),))],
        [sg.Text('File 2'), sg.Input(disabled=True, size=(80,1), expand_x=True), sg.FileBrowse(file_types=(('DeltaV Config Files','*.fhx'),))],
        [sg.Button('Show Filters', key='-EXPAND-'), sg.Submit('Compare'), sg.Cancel()],
        [sg.Frame('Filters', filter_frame, visible=False, expand_x=True, key='-FILTERS-')]
        ]
    window = sg.Window('Phase Compare', layout, size=(750,150))
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"Cancel"):
            window.close()
            return None
        elif (event == 'Compare') and values[0] and values[1]:
            window.close()
            if not values['-CONTEXT-']:
                values['-CONTEXT-'] = 0
            return values
        elif event == '-EXPAND-':
            if flag == 0:
                window['-FILTERS-'].update(visible=True)
                window['-EXPAND-'].update(text='Hide Filters')
                flag = 1
                window.size = (750,250)
                window.refresh()
            elif flag == 1:    
                window['-FILTERS-'].update(visible=False)
                window['-EXPAND-'].update(text='Show Filters')
                window.size = (750,150)
                window.refresh()
                flag = 0
        elif event == '-CONTEXT-' and values['-CONTEXT-'] and values['-CONTEXT-'][-1] not in ('0123456789'):
            window['-CONTEXT-'].update(values['-CONTEXT-'][:-1])
                


def showhtml(filename):
    # lazy solution of letting browsers handle it
    webbrowser.open('file://' + os.path.realpath(filename))