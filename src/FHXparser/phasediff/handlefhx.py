def filterread(params, file):
    lines = list()
    with open(file,  'r', encoding='utf', errors='replace') as ff:
        strippara = None
        filterpara = list()
        skipconf = 0
        if params['-WHITE-']:
            if params['-BRACE-']:
                strippara = ' {}'
        if params['-LINE-']:
            filterpara += ['X=', 'Y=']
        if params['-COMMENT-']:
            skipconf = 1
            filterpara += ['/*', '*/']
        if params['-EC-']:
            filterpara.append('__')
        for l in ff:
            if skipconf:
                if 'STEP NAME=' not in l:
                    continue
                skipconf = 0
            if any(i in l for i in filterpara):
                continue
            lines.append(l.strip(strippara))
    return lines