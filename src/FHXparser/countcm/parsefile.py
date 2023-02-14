from . import handlecsv
def countmodconf(fileName, outputPath, modulePrefix):
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
                handlecsv.writecount(outputPath, [fileName, moduleName, LC, EC, FB, PARA, ALARM])
                # reset flag and counters
                LC = EC = FB = PARA = ALARM = int()
                flag = 'mod'
    return 'File ' + fileName[:-4] + ' completed.'