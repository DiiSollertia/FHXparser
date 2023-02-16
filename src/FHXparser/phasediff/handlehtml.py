import difflib as dl
from . import handlefhx

def makehtml(params):
    file1, file2 = params[0], params[1]
    fromlines = handlefhx.filterread(params, file1)
    tolines = handlefhx.filterread(params, file2)
    return dl.HtmlDiff().make_file(fromlines,tolines,file1,file2,context=True,numlines=int(params['-CONTEXT-']))

def writehtml(htmlstring, location):
    output = location + '/difftable.html'

    # limit table size
    htmlstring = htmlstring.replace("</style>","\ttd{max-width: 40vw;overflow-x: auto;}\n\t</style",1)

    with open(output,'w') as f:
        f.write(htmlstring)
    return output