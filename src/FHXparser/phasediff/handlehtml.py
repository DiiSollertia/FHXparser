import difflib as dl

def makehtml(params):
    file1, file2 = params[0], params[1]
    fromlines = customfilter(params, file1)
    tolines = customfilter(params, file2)
    return dl.HtmlDiff().make_file(fromlines,tolines,file1,file2,context=True,numlines=int(params['-CONTEXT-']))

def writehtml(htmlstring, location):
    output = location + '/difftable.html'

    # limit table size
    htmlstring = htmlstring.replace("</style>","\ttd{max-width: 40vw;overflow-x: auto;}\n\t</style",1)

    with open(output,'w') as f:
        f.write(htmlstring)
    return output

def customfilter(params, file):
    lines = list()
    with open(file,  'r', encoding='utf-16') as ff:
        strippara = None
        filterpara = list()
        if params['-WHITE-']:
            if params['-BRACE-']:
                strippara = ' {}'
        if params['-LINE-']:
            filterpara += ['X=', 'Y=']
        if params['-COMMENT-']:
            filterpara += ['/*', '*/']
        if params['-EC-']:
            filterpara.append('__')
        for l in ff:
            if any(i in l for i in filterpara):
                continue
            lines.append(l.strip(strippara))
    return lines