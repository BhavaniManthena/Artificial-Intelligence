import random
import copy
import math
dictionary={}
np=10
nc=100
F=0.8
CR=0.1
copydictionary={}
minlist=[]


def ackely(x,y):
    f=((-20)*math.exp((-0.2)*math.sqrt(0.5*(math.pow(x,2)+math.pow(y,2))))) - math.exp((0.5)*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y)))
    return f

#listx=[]
#listy=[]
#a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]#random list for r0,r1,r2
for iterations in range(0,100):
    for i in range(0,10):
        x=random.uniform(-5,5)
        #listx.append(x)
        y=random.uniform(-5,5)
        #listy.append(y)
        #integerlist=[x,y]
        copydictionary[i]=(x,y)
    #print(dictionary)
    for p in range(0,nc):
        dictionary=copy.copy(copydictionary)
        for i in range(0,np):
            myrand = random.sample(range(0,10),3)
            for k in range(0,100):
                if i not in myrand:
                    break
                else:
                    myrand = random.sample(range(0,10),3) 
            vectorx=dictionary[myrand[0]][0]+(F*(dictionary[myrand[1]][0]-dictionary[myrand[2]][0]))
            vectory=dictionary[myrand[0]][1]+(F*(dictionary[myrand[1]][1]-dictionary[myrand[2]][1]))
            u=random.uniform(0,1)
            if u < CR:
                vectorux=copy.copy(vectorx)
            else:
                vectorux=dictionary[i][0]

            unew=random.uniform(0,1)
            if unew < CR:
                vectoruy=copy.copy(vectory)
            else:
                vectoruy=dictionary[i][1]
            funvar=ackely(vectorux,vectoruy)
            funxi=ackely(dictionary[i][0],dictionary[i][1])
            if funvar<funxi:
                copydictionary[i] = (vectorux,vectoruy)
            else:
                copydictionary[i] = dictionary[i]
    #print(copydictionary)
    for i in range(0,10):
        minlist.append(ackely(copydictionary[i][0],copydictionary[i][0]))
    #print(minlist)//number of populations in a list
    print(min(minlist))
    del minlist[:]  
