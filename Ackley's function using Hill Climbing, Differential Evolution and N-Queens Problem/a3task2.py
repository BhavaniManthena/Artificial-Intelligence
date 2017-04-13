import time 
import sys
import copy
start_time = time.clock()
file = {}
finaldict=[]
with open('dictionary.txt', 'r') as dictionary:
    data = dictionary.read().splitlines()
    for number in range(3,9):
        group = []
        for line in data:
            if(len(line)==number):
                group.append(line)
                finaldictallwords[number]=group
    print (finaldictallwords)
#divided into only 1 file
#for 2,3,4,5 len dictionaries
for word in finaldict:
    if(word.len==2):
        len2+=word
    else if(word.len==3):
        len3+=word
    else if(word.len==4):
        len4+=word
    else if(word.len==5):
        len5+=word
    else if(word.len==6):
        len6+=word
    else
        len7+=word

def word1():
	global flag1
	len3[1] = finaldict[1][flag1]
	nextword()

def nextword():
    for word in 
	global flag1
	global flag2
	global flag3
	global flag4
	global flag5
	global flag6
	len=[]
	for k in range(0,5):
	    if (finaldict[2][k][0]==finaldict[1][2]):
		list1.append(finaldict[2][k])
	if not len3:
	    flag1=flag1+1
            word1()
	else if not len4:
            finaldict[2]=len2[flag2]
            flag3=0
            nextword()
	else if not len5:
            flag4=0
	    flag5=0
	    finaldict[3]=len2[flag3]
	    nextword()
	else if not len6:
            flag6=flag6+1
	    del finaldict[6]
            del finaldict[7]
	    flag5=flag5+1	
	    len6(flag6)
	else:
            finaldict[8]=len7[0]
	    print finaldict
		
