import os

basedir = os.getcwd()
for fn in os.listdir(basedir):
    try:
        if fn[0:4] == "The " or fn[0:4] == "The.":
            oldpathName = os.path.join(basedir,fn)
            newpathName = os.path.join(basedir,fn[4:])
            os.rename(oldpathName, newpathName)
    except:
        print fn
print "Complete"
input()
