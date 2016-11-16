import os

filmNames = []
output = ""
basedir = os.getcwd()
for fn in os.listdir(basedir):
    num = 0
    secdir = os.path.join(basedir,fn)
    if os.path.isdir(secdir):
        filmNames += [fn]



for fullName in filmNames:
    yearStart = 0
    yearEnd = 0
    qualityStart = 0
    qualityEnd = 0
    for i in range(len(fullName)):
        if fullName[i] == "(":
            yearStart = i
        elif fullName[i] == ")":
            yearEnd = i
        if fullName[i] == "[":
            qualityStart = i
        elif fullName[i] == "]":
            qualityEnd = i

    name = fullName
    year = ""
    quality = ""
    if yearStart != 0:
        name = fullName[:(yearStart-1)]
        year = fullName[yearStart:yearEnd+1]
    if qualityStart != 0:
        quality = fullName[qualityStart:qualityEnd+1]
    output += name + "\t" + year + "\t" + quality + "\n"
f = open("name.txt","w")
f.write(output)
f.close()
os.startfile("name.txt")
print "Complete"
#input()
