import os
lenth = 18

def checkRepeat(pa):
    global lenth
    for fn in os.listdir(pa):
        if fn == "sample" or fn == "Sample" or fn == "Cover" or fn == "cover":
            print pa[lenth:]
        curDir = os.path.join(pa,fn)
        if os.path.isdir(curDir):
            checkRepeat(curDir)
        elif fn[-4:] == ".nfo" or fn[-4:] == ".NFO":
            try:
                os.remove(curDir)
            except:
                print pa[lenth:]
        elif fn[-4:] == ".txt":
            try:
                os.remove(curDir)
            except:
                print pa[lenth:]
        elif fn[-6:] == ".cache":
            try:
                os.remove(curDir)
            except:
                print pa[lenth:]
        
        elif fn[-4:].lower() == ".jpg" or fn[-4:] == ".png":
            try:
                os.remove(curDir)
            except:
                print pa[lenth:]

        elif fn == "ETRG.mp4":
            try:
                os.remove(curDir)
            except:
                print pa[lenth:]
        elif fn[-4:] == ".htm":
            try:
                os.remove(curDir)
            except:
                print pa[lenth:]
        elif fn.lower()[:4] == "etrg" or fn.lower()[:6] == "sample":
            try:
                os.remove(curDir)
            except:
                print pa[lenth:]
basedir = os.getcwd()


checkRepeat(basedir)
print "Complete"
input()
