import PySimpleGUI as sg

def selectmode():
    layout = [
        [sg.Text('Choose a mode to parse FHX:')],
        [sg.Submit('Control Module Elements Counter'), sg.Submit('Compare Phases'), sg.Cancel('Exit')],
        ]
    window = sg.Window('FHXparser', layout)
    event = window.read()[0]
    window.close()
    return event