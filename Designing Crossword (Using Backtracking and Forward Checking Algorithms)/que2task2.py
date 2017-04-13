import copy
import random
dictionary8={}
dictionary16={}
nonheu={}
parent1=[]
parent2=[]
m=0
n=99
value=0
spot=0
option=0
total8q=0
total16q=0
def crossover(parent1,parent2):
    c1=[]
    inc=0
    n=6
    for i in range(3,n):
        c1.append(parent1[i])
    for i in range(n,len(parent2)):
        if(parent2[i] not in c1):
            c1.append(parent2[i])
    for i in range(0,n):
        if(parent2[i] not in c1):
            if(len(c1)>=5):
                c1.insert(inc,parent2[i])
                inc=inc+1
            else:
                c1.append(parent2[i])
    #print(c1)
    return c1
def heuristic(c1):
    c=1
    count=0
    length=len(c1)
    for i in range(length):
        c=1
        for j in range(i+1,length):
            if c1[i]==c1[j]:
                count=count+1
            if c1[i]-c==c1[j] and i+c==j:
                count=count+1
            if c1[i]+c==c1[j] and i+c==j:
                count=count+1
            c=c+1
    #print(count)        
    return count
option=input(" 8 or 16 queens")
option=int(option)
if(option==8):
    print("for 8 queens")
    for i in range(0,100):
        parent=[0,1,2,3,4,5,6,7]
        random.shuffle(parent)
        dictionary8[i]=parent
    for j in range(0,99):
        m=0
        n=99
        spot=0
        nonheu={}
        #print("non heuristic dictionary")
        #print(nonheu)
        for i in range(0,50):
            c1 = crossover(dictionary8[m],dictionary8[n])
            count=heuristic(c1)
            if(count==0):
                print(c1)
                total8q=total8q+1                
            else:
                nonheu[spot]=c1
                spot=spot+1
            m=m+1
            n=n-1
            #print(value)
            value=value+1
            if(m>=n):
                break
        nhvalue=len(nonheu)
        for i in range(nhvalue,100):
            parent=[0,1,2,3,4,5,6,7]
            random.shuffle(parent)
            nonheu[i]=parent
        dictionary8.clear()
        dictionary8=nonheu
    print("total heuristics are",total8q)
if(option==16):
    for i in range(0,100):
        parent=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        random.shuffle(parent)
        dictionary16[i]=parent
    for j in range(0,99):
        m=0
        n=99
        spot=0
        nonheu={}
        #print("non heuristic dictionary")
        #print(nonheu)
        for i in range(0,50):
            c1 = crossover(dictionary16[m],dictionary16[n])
            count=heuristic(c1)
            if(count==0):
                print("heuristic")
                total16q=total16q+1 
            else:
                nonheu[spot]=c1
                spot=spot+1
            m=m+1
            n=n-1
            #print(value)
            value=value+1
            if(m>=n):
                break
        nhvalue=len(nonheu)
        for i in range(nhvalue,100):
            parent=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            random.shuffle(parent)
            nonheu[i]=parent
        dictionary16.clear()
        dictionary16=nonheu
    print("total heuristics are",total16q)
