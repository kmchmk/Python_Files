import os

try:
    start = input("Enter the starting no.: ")
    end = input("Enter the last no.: ")
    for i in range(start,end+1):
        
        no = "0"*(len(str(end))-len(str(i))) + str(i)
        newpath = os.getcwd()+'/E'+no
        if not os.path.exists(newpath):
            os.makedirs(newpath)
    print "Folder from E"+str(start)+" to E"+str(end)+" is created"
except:
    print "Job couldn't be done correctly"


