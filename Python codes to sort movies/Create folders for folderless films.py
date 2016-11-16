import os

basedir = os.getcwd()

for fn in os.listdir(basedir):
    if not os.path.exists(fn):
        os.makedirs(fn[:-4])
        



print "Complete"
input()
