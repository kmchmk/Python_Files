while(True):
    num = raw_input()
    first = ['','one', 'two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    second = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    third = ['','thousand','million','billion','trillion']
    word = ''

    numberofparts = (len(num) + 2)/3
    for i in range(numberofparts):
        tempnum = ''
        if(len(num)>3):
            tempnum = str(int(num[-3:]))
            num = num[:-3]
        elif(len(num)>0):
            tempnum = str(int(num))
            num = ''
        else:
            break


        if(int(tempnum) < 20):
            word1 = first[int(tempnum)]
        else:
            word1 = ''
            numlist = map(int,list(tempnum))
            length = len(numlist)
            if(length == 2):
                word1 = second[numlist[0]] +' '+ first[numlist[1]]
            elif(length == 3):
                if(numlist[1]<2):
                    word1 = first[numlist[0]] +' hundred '+' '+ first[int(str(numlist[1]) + str(numlist[2]))]
                else:
                    word1 = first[numlist[0]] +' hundred '+ second[numlist[1]]+' '+ first[numlist[2]]
        if(int(tempnum)==0):
            word =  word1 +' ' + word 
        else:
            word =  word1 +' '+ third[i] + ', ' + word 


    print word[:-3] + '.'



