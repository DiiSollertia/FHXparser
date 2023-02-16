import PySimpleGUI as sg
import os
from . import parsefile

def selectfiles():
    mode = selectmode()
    layout = setlayout(mode)
    window = sg.Window('Count Control Module Elements', layout)
    while True:
        event, values = window.read()
        if event == 'Start Count':
            try:
                if fnames:
                    window.close()
                    return fnames
            except UnboundLocalError:
                continue
        if event in (sg.WINDOW_CLOSED,'Cancel'):
            window.close()
            return
        if event == '-BROWSE-':
            folder = values['-BROWSE-']
            try:
                # is actually folder
                file_list = os.listdir(folder)
                fnames = [folder + '/' + f for f in file_list if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".fhx"))]
                window['-FILES-'].update(fnames)
            except:
                # is actually file or empty
                fnames = folder.split(';')
                window['-FILES-'].update(fnames)
        elif event == 'Change Mode':
            window.close()
            window = sg.Window('Count Control Module Elements', setlayout(selectmode()))

def selectmode():
    return sg.Window('Select Mode',[[sg.Button('Files'), sg.Button('Folder') ]]).read(close=True)[0]

def setlayout(mode):
    if mode == 'Files':
        layout = [
            [sg.Text('Select 1 or more files.')],
            [sg.FilesBrowse(enable_events=True, file_types=[('DeltaV Config Files','*.fhx')],key='-BROWSE-')],
            ]
    elif mode == 'Folder':
        layout = [
            [sg.Text('Select a folder.')],
            [sg.FolderBrowse(enable_events=True,key='-BROWSE-')],
        ]
    layout.append([
        [sg.Listbox(values=[], enable_events=True, horizontal_scroll=True, size=(80,10), key='-FILES-') ],
        [sg.Submit('Start Count'), sg.Submit('Change Mode'), sg.Cancel()],
        ])
    return layout

def selectprefix():
    layout = [
        [sg.Text('Enter module prefix to filter or simply Submit to continue. (Ex. "XV_", "EM_", "TIC_", etc. without quotation marks)')],
        [sg.Input(expand_x=True), sg.Submit()]
    ]
    window = sg.Window('Filter by Prefix', layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Submit'):
            window.close()
            return values[0]

def loadingbar(filelist, outputpath, moduleprefix):
    layout = [
            [sg.Text('Parsing FHX...', key='-TEXT-')],
            [sg.ProgressBar(len(filelist), orientation='h', size=(40, 20), key='-PROGRESS-')],
        ]
    window = sg.Window('Parsing...', layout, finalize=True)
    progressbar = window['-PROGRESS-']
    for i, filename in enumerate(filelist):
        window['-TEXT-'].update(parsefile.countmodconf(filename, outputpath, moduleprefix))
        progressbar.UpdateBar(i+1)
    window.close()

def success(outputpath):
    layout = [
        [sg.Text('Process completed.')],
        [sg.Text('Output generated in ' + outputpath)],
        [sg.OK()],
    ]
    window = sg.Window('Success.', layout)
    window.read()
    window.close()