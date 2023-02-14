import difflib

def makehtml(file1, file2):
    with open(file1) as ff:
        fromlines = ff.readlines()
    with open(file2) as tf:
        tolines = tf.readlines()
    return difflib.HtmlDiff().make_file(fromlines,tolines,file1,file2,context=True,numlines=1) 

def writehtml(htmlstring, location):
    with open(location + '/difftable.html','w') as f:
        f.write(htmlstring)