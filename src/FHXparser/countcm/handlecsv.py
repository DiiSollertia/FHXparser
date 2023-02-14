import csv
import sys

def writeheader(filePath):
    headerList = ['FileName', 'ModuleName', 'LinkedComposites', 'EmbeddedComposites', 'FunctionBlocks', 'Parameters', 'Alarms']
    output = str(filePath) + '/output.csv'
    
    for i in range(5, 0, -1):
        try:
            print(output)
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

def writecount(output, counters):
    with open(output, 'a', newline='') as csvfile:
        Filler = csv.writer(csvfile, dialect='excel', delimiter=',')
        Filler.writerow(counters)
    return 'Module ' + str(counters[1]) + ' completed.'