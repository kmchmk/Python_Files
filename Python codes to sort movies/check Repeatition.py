import os

basedir = os.getcwd()
for fn in os.listdir(basedir):
    num = 0
    secdir = os.path.join(basedir,fn)
    if os.path.isdir(secdir):
        for vid in os.listdir(secdir):
            if not os.path.isdir(os.path.join(secdir,vid)):
                if vid[-4:].lower() == ".mkv" or vid[-4:].lower() == ".mp4" or vid[-4:].lower() == ".flv" or vid[-4:].lower() == ".wmv" or vid[-4:].lower() == ".avi" or vid[-4:].lower() == ".vob" or vid[-4:].lower() == "divx":
                    num += 1
        if num != 1:
            try:
                print fn
                #os.startfile(secdir)
            except:
                print "Couldn't open " + fn

print "Complete"
input()
