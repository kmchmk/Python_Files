import os

basedir = os.getcwd()
for fn in os.listdir(basedir):
    secdir = os.path.join(basedir,fn)
    if os.path.isdir(secdir):
        for vid in os.listdir(secdir):
            thirdir = os.path.join(secdir,vid)
            if os.path.isdir(thirdir) and vid != "sub":
                os.startfile(secdir)

print "Complete"
input()
