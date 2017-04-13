import time
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
answerdict={}
flag3=0
flag6=0
flag2=0
flag5=0
flag4=0
flag1=0
start_time = time.clock()
worddict={1:['LASER','STEER','SAILS','SHEET','HOSES'],2:['HOSES','LASER','STEER','SHEET','SAILS'],3:['STEER','LASER','SAILS','SHEET','LASER'],4:['HEEL','HIKE','KNOT','KEEL','LINE'],5:['HEEL','HIKE','KNOT','KEEL','LINE'],6:['AFT','EEL','ALE','LEE','TIE'],7:['AFT','EEL','ALE','LEE','TIE'],8:['HOSES','STEER','SAILS','SHEET','LASER']}


def word1():
	global flag1
	answerdict[1] = worddict[1][flag1]
	#print answerdict
	word2()

def word2():
	global flag1
	global flag2
	global flag3
	list1=[]
	for k in range(0,5):
		if (worddict[2][k][0]==answerdict[1][2]):
			list1.append(worddict[2][k])
	if not list1:
		flag1=flag1+1
		word1()
	else:
		answerdict[2]=list1[flag2]
		flag3=0
		word3()
		
def word3():
	global flag4
	global flag2
	global flag5
	global flag1
	global list2
	if (flag3 < len(list2) or flag3 == 0):
		list2=[]
		for l in range(0,5):
			if (worddict[3][l][0]==answerdict[1][4]):
				list2.append(worddict[3][l])
		if not list2:
			flag1=flag1+1
			word1()
		else:
			flag4=0
			flag5=0
			answerdict[3]=list2[flag3]
			#print "at word3",answerdict
			word4(flag4)
	else:
		flag2=flag2+1
		#print "flag2",flag2
		word2()
def word4(flag4):
	global flag3
	global flag6
	global flag5
	global list3
	#print "mine",answerdict
	#print "flag4",flag4
	#print "flag5 in word4", flag5
	if (flag4 < len(list3) or flag4 == 0):
		list3=[]
		for m in range(0,5):
			if(worddict[4][m][1]==answerdict[2][2] and worddict[4][m][3]==answerdict[3][2]):
				list3.append(worddict[4][m])
		#print list3
		if not list3:

			flag3=flag3+1
			word3()
		else:
			#print flag4
			if (flag6 >4):
				del answerdict[flag6]
				flag6=0	
			#print list3[flag4]
			answerdict[4]=list3[flag4]
			word5(flag5)
	else:
		flag3=flag3+1
		#print "flag3",flag3
		word3()


def word5(dummyflag5):

	global flag6
	global list4
	global flag4
	global flag5

	#print "flag6",flag6
	#print "flag5",flag5
	#print answerdict
	#print len(list4)
	if (flag5 < len(list4) or flag5 == 0):
		list4=[]
		for n in range(0,5):
			if(worddict[5][n][0]==answerdict[4][2]):
				list4.append(worddict[5][n])
		#print list4
		if not list4:
			del answerdict[4]
			word4(flag4)
		else:

			answerdict[5]=list4[flag5]
			#print "k",answerdict[5]
			word6(flag6)
	else:
		flag4=flag4+1
		#print "flag4",flag4
		#print "entered flag4"
		#print "flag5=" + str(flag5)
		word4(flag4)

def word6(flag6):
	global list5
	global flag5
	#print flag6
	#print len(list5)
	if (flag6 < len(list5) or flag6 == 0):
		list5=[]
		for o in range(0,5):
				list5.append(worddict[6][o])
		#print list5

		answerdict[6]=list5[flag6]
		#print "new",answerdict[6]
		word7()
	else:
		#print "entered word5"
		flag5=flag5+1
		#print "flag5",flag5
		#print answerdict
		word5(flag5)

def word7():
	global list6
	#print answerdict
	global flag4
	global flag5
	global flag6
	list6=[]
	for p in range(0,5):
		if(worddict[7][p][0]==answerdict[2][3] and worddict[7][p][1]==answerdict[5][1] and worddict[7][p][2]==answerdict[3][3]):
			list6.append(worddict[7][p])

	#print list6
	if not list6:
		#print list5
		flag5=flag5+1
		#print "flag5",flag5
		flag6=0
		word5(flag5)
	else:
		answerdict[7]=list6[0]
		flag5=0
		word8()
def word8():
	global flag6
	global flag5
	#print answerdict[6]
	for q in range(0,5):	
		if (worddict[8][q] not in answerdict.values()):
			#print worddict[8][q]
			#print answerdict
			if(worddict[8][q][0]==answerdict[6][1] and worddict[8][q][2]==answerdict[2][4] and worddict[8][q][3]== answerdict[5][2] and worddict[8][q][4]== answerdict[3][4]):
				list7.append(worddict[8][q])
	if not list7:
	  	flag6=flag6+1
		del answerdict[6]
		del answerdict[7]
		flag5=flag5+1	
		word6(flag6)
	else:
		answerdict[8]=list7[0]
		print answerdict


word1()	
print time.clock() - start_time, "seconds"
