import random as rm
words=[]
temp=[]
lastchar1=''
lastchar2=''
f1=open('dictionary.txt','r')
words=[i.replace('\n' ,'') for i in f1.readlines()]
index1=rm.randrange(0,len(words)+1)
computerchoice=words[index1]
print('Computer :',computerchoice)
lastchar1= computerchoice[-1]
words.remove(computerchoice)
while True:
    userchoice=input('user : ')
    if userchoice in words and userchoice.startswith(lastchar1):
        words.remove(userchoice)
        lastchar2=userchoice[-1]
        temp=list(filter(lambda i: i.startswith(lastchar2),words))
        index2=rm.randrange(0,len(temp)+1)
        computerchoice=temp[index2]
        lastchar1=computerchoice[-1]
        print('Computer :',computerchoice)
        words.remove(computerchoice)
    else:
        print('computer wins')
        break
        







        

