import os

basedir = os.getcwd()
for fn in os.listdir(basedir):
    #print fn
    #if not os.path.isdir(os.path.join(basedir, fn)):
        #continue # Not a directory
  #if ',' in fn:
    #continue # Already in the correct form
  #if ' ' not in fn:
    #continue # Invalid format
    #firstname,_,surname = fn.rpartition(' ')
    if(fn[0] != "E" and fn[0] != "r"):
        if(int(fn)<10):
            os.rename(os.path.join(basedir, fn),os.path.join(basedir, "E0"+fn))
        else:
            os.rename(os.path.join(basedir, fn),os.path.join(basedir, "E"+fn))

    if(fn[0] == "E" ):        
        for ep in os.listdir(os.path.join(basedir,fn)):
            if(ep[-3:] == "mp4" or ep[-3:] == "mkv" or ep[-3:] == "avi"):
                video = ep
            if(ep[-3:] == "srt" or ep[-3:] == "ssa"):
                sub = ep
            else:
                print "error in "+ep
        if(sub[-3:] == "srt"):
            os.rename(os.path.join(os.path.join(basedir, fn), sub), os.path.join(os.path.join(basedir, fn), video[:-3]+"srt"))
        elif(sub[-3:] == "ssa"):
            os.rename(os.path.join(os.path.join(basedir, fn), sub), os.path.join(os.path.join(basedir, fn), video[:-3]+"ssa"))


print "Complete"
