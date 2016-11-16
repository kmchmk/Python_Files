from datetime import datetime as dt1
import datetime as dt2

def addSecs(string, secs):
    return (dt1.strptime(string, '%H:%M:%S') + dt2.timedelta(seconds=secs)).strftime('%H:%M:%S')

noOfSecs = input("Enter secs: ")

#get the number lines in the file
f1 = open("a.srt","r")
numberOfLines = len(f1.readlines())
f1.close()
#print "Number of lines: "+ str(numberOfLines)

nf = open("b.srt","w+")

f = open("a.srt","r")
lineNumber = 2
i = 0
while(i < numberOfLines):
    try:
        line = f.readline()
        i += 1
        try:
            num = int(line)
            nf.write(line)
            t = f.readline()
            numberOfLines += 1
            newtimeline = addSecs(t[:8],noOfSecs) + t[8:17]+ addSecs(t[17:25], noOfSecs) + t[25:]

            nf.write(newtimeline)
            
            if(lineNumber != num):
                print "line " + str(lineNumber) + " is missing"
                break
            lineNumber += 1
        except:
            nf.write(line)
    except:
        break

f.close()
nf.close()

print("complete")
