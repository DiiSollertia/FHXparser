#!/usr/bin/env python
import os
import csv
import sys
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilenames

def main():
    pathMode = int(input('Enter:\n"1" to select a folder.\n"2" to select files.\n\nSelect Mode:'))
    workingPath, fileList = selectPath(pathMode)
    outputPath = writeHeader(workingPath)
    modulePrefix = input('Enter module prefix to filter or simply press ENTER to continue.\n(Ex. "XV", "EM", "TIC", etc. without quotation marks)\nFilter: ')
    modulePrefix = modulePrefix.upper()
    for fileName in fileList:
        print(countFile(fileName, outputPath, modulePrefix))
    return 'Process completed.\nOutput generated in ' + outputPath

def selectPath(mode, attempt=5):
    root = tk.Tk()
    fileList = list()
    if mode == 1:
        # Folder mode
        print('Please select a folder containing FHX files.')
        workingPath = askdirectory(title='Select Folder')
        # Recursive if no files selected
        if checkEmpty(workingPath, attempt):
            workingPath, fileList = selectPath(mode, attempt - 1)
        fileList = [(workingPath + '/' + filename) for filename in os.listdir(workingPath) if filename.endswith('.fhx')]
        if checkEmpty(fileList, attempt):
            workingPath, fileList = selectPath(mode, attempt - 1)
    elif mode == 2:
        # Files mode
        print('Please select the FHX files.')
        fileList = askopenfilenames(title='Select FHX', filetypes=[('DeltaV Config Files','*.fhx')])
        # Recursive if no files selected
        if checkEmpty(fileList, attempt):
            workingPath, fileList = selectPath(mode, attempt - 1)
        workingPath = os.path.dirname(fileList[0])
    root.withdraw()
    return workingPath, fileList

def checkEmpty(obj, attempt):
    # Recursive if no files selected
    if not obj:
        if attempt == 0:
            input('Exceeded retry limit. Press ENTER to exit.')
            sys.exit()
        print('Attempts left: ' + str(attempt))
        return True
    return False

def writeHeader(filePath):
    headerList = ['FileName', 'ModuleName', 'LinkedComposites', 'EmbeddedComposites', 'FunctionBlocks', 'Parameters', 'Alarms']
    output = str(filePath) + '/output.csv'
    
    for i in range(5, 0, -1):
        try:
            with open(output, 'w', newline='') as csvfile:
                HeaderWriter = csv.writer(csvfile, dialect='excel', delimiter=',')
                HeaderWriter.writerow(headerList)
        except PermissionError:
            print('Attempts left: ' + str(i))
            input('Please close "output.csv". Press ENTER to continue.')
        else:
            break
    else:
        input('Exceeded retry limit. Press ENTER to exit.')
        sys.exit()
    return output

def countFile(fileName, outputPath, modulePrefix):
    print('Processing: ' + fileName)
    with open(fileName, 'r', encoding='utf-16') as f:
        LC = EC = FB = PARA = ALARM = int()
        flag = 'mod'
        for line in f:
            # check for module
            if (flag == 'mod'):
                if line[:10] == 'MODULE TAG':
                    flag = 'ec'
                    moduleName = line[12:line.find('"',12)]
                    
                    # only scan valves
                    if modulePrefix and (moduleName[:len(modulePrefix)] != modulePrefix):
                        flag = 'mod'
                        continue
            # check for embedded composite
            elif flag == 'ec':
                if line[2:11] == 'ATTRIBUTE':
                    flag = 'alarm'
                    # one-off check since the flag is triggered in same row to reduce time-complexity
                    if 'TYPE=EVENT' in line[19:]:
                        PARA -= 1
                        ALARM += 1
                elif line[2:16] == 'FUNCTION_BLOCK':
                    if '__' in line[26:]:
                        EC += 1
                    else:
                        flag = 'lc'
            # check for linked composite / function block
            elif flag == 'lc':
                if line[4:8] == 'DESC':
                    FB += 1
                    LC -= 1
                elif line[4:7] == 'ID=':
                    LC += 1
                    flag = 'ec'
            # ignore alarms / events
            elif flag == 'alarm':
                if line[2:10] == 'FBD_ALGO':
                    flag = 'para'
                elif 'TYPE=EVENT' in line[19:]:
                    PARA -= 1
                    ALARM += 1
            # check for parameter
            elif flag == 'para':
                if line[2:20] == 'ATTRIBUTE_INSTANCE':
                    if '/' in line[27:]:
                        flag = 'done'
                    else:
                        PARA += 1
            elif flag == 'done':
                print(writeCount(outputPath, [fileName, moduleName, LC, EC, FB, PARA, ALARM]))
                # reset flag and counters
                LC = EC = FB = PARA = ALARM = int()
                flag = 'mod'
    return 'File ' + fileName[:-4] + ' completed.'

def writeCount(output, counters):
    with open(output, 'a', newline='') as csvfile:
        Filler = csv.writer(csvfile, dialect='excel', delimiter=',')
        Filler.writerow(counters)
    return 'Module ' + str(counters[1]) + ' completed.'

if __name__ == '__main__':
    main()
    input('Press ENTER to close.')