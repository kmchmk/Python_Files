import os


def unwanted(pat):
    lis = ["srt","mp4","ssa","idx","sub","avi","flv","mkv",".db","ass","vob"]
    for fn in os.listdir(pat):
        secdir = os.path.join(pat,fn)
        if os.path.isdir(secdir):
            for vid in os.listdir(secdir):
                thirdir = os.path.join(secdir,vid)
                if os.path.isdir(thirdir):
                    unwanted(thirdir)
                else:
                    if vid[-3:].lower() not in lis:
                    #if vid[-3:].lower() == ".db":
                        print vid[-3:].lower()
                        os.startfile(secdir)



basedir = os.getcwd()
unwanted(basedir)

print "Complete"
input()
