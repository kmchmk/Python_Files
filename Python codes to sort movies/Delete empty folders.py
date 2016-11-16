import os

basedir = os.getcwd()
def isEmpty(basedir):
    try:
        for fn in os.listdir(basedir):
            empty = True
            secdir = os.path.join(basedir,fn)
            if os.path.isdir(secdir):
                isEmpty(secdir)
                for vid in os.listdir(secdir):
                    empty = False
                if empty == True:
                    try:
                        print fn
                        #os.startfile(secdir) #to open
                        try:
                            os.remove(secdir) #to remove
                        except:
                            print "Couldn't delete " + fn
                            os.startfile(secdir)
                    except:
                        print "Couldn't open " + fn
                        os.startfile(secdir)
    except:
        print "cannot access " + fn
maindir = os.getcwd()
isEmpty(maindir)
print "Complete"
input()
