import difflib as dl

def makehtml(file1, file2):
    with open(file1,  'r', encoding='utf-16') as ff:
        fromlines = [l.strip() for l in ff if l.strip()]
    with open(file2,  'r', encoding='utf-16') as tf:
        tolines = [l.strip() for l in tf if l.strip()]
    return dl.HtmlDiff().make_file(fromlines,tolines,file1,file2,context=True,numlines=0)

def writehtml(htmlstring, location):
    output = location + '/difftable.html'
    with open(output,'w') as f:
        f.write(htmlstring)
    return output