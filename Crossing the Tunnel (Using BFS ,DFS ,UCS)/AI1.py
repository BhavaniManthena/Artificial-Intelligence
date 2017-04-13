from random import randint
import sys	
from collections import OrderedDict
from itertools import combinations
import copy
import time 
#front function to move 2 persons from right to left side of the bridge
def front(mynext,incrementor1):
	dummylistfwd =[]
	a=mynext
	y=a.index('!')
	b= a[:y]
	for u in combinations(b,2):
		global incrementor
		u=list(u)
		costdict[incrementor+1] = max(u)
		c=copy.copy(a)
		for i in u:
			c.remove(i)
		for i in u :
			c.append(i)
		childlist.append(c)
		incrementor=incrementor+1
		childdict[incrementor] = incrementor1
		dummylistfwd.append(incrementor)
		completedict[incrementor]=c
	parentdict[incrementor1]= dummylistfwd
	return incrementor
incrementor1=2
#Back function to move 1 persons from left to right side of the bridge
def back(b,incrementor1):
	dummylistfwd =[]
	y=b.index('!')
	a=b[y+1:]
	for p in combinations(a,1):
		global incrementor
		p=list(p)	
		costdict[incrementor+1] = max(p)
		f=copy.copy(b)
		for i in p:
			f.remove(i)
			f=[i]+f
			childlist.append(f)
			incrementor=incrementor+1
			childdict[incrementor] = incrementor1
			dummylistfwd.append(incrementor)
			completedict[incrementor]=f
	parentdict[incrementor1]= dummylistfwd
	return childlist
#function which does bredthfirstsearch 
def bredthfirstsearch():	
	queue_list = []
	parent=[]
	i=1
	queue_list.append(i)
	while True:
		if (completedict[queue_list[0]][0]=='!'):
			parent.append(queue_list[0])
			b=queue_list[0]
			while True:
				a=childdict[b]
				parent.append(a)
				b=a
				if(a == 1):
					break
			break
		temp = queue_list[0]
		queue_list.pop(0)
		queue_list=queue_list+parentdict[temp]	
	length =len(parent)
	parent.reverse()
	sum=0
	for c in range (0,length):
		a=parent[c]
		if (c>0):
			v=costdict[a]
			sum = sum + v
			print "Stage %s takes %s seconds" %(c,v)
		print completedict[a]
	print "Total Time taken to pass all the people from one end to other end is %s"%sum
	
#function which does depthfirstsearch 
def depthfirstsearch():
	stack_list = []
	new_parent=[]
	i=1
	stack_list.append(i)
	while True:
		if(completedict[stack_list[0]][0]=='!'):
			new_parent.append(stack_list[0])
			b=stack_list[0]
			while True:
				a=childdict[b]
				new_parent.append(a)
				b=a
				if (a==1):
					break
			break
		temp = stack_list[0]
		stack_list.pop(0)
		stack_list=parentdict[temp]+stack_list
	length =len(new_parent)
	new_parent.reverse()
	sum=0
	for c in range (0,length):
		a=new_parent[c]
		if (c>0):
			v=costdict[a]
			sum = sum + v
			print "Stage %s takes %s seconds" %(c,v)
		print completedict[a]
	print "Total Time taken to pass all the people from one end to other end is %s"%sum
#function which does uniformcostsearch 
def uniformcostsearch():
	pri_que_list =[]
	dummy = []
	new_list=[]
	i=0
	pre_dict={}
	dummy=parentdict[1]
	for i in dummy:
		pre_dict[i]=costdict[i]
	b= sorted(pre_dict.items(),key=lambda t:t[1])
	while True:
		c=b[0][0]
		del pre_dict[c]
		for i in parentdict[c]:
			pre_dict[i]=costdict[i]+b[0][1]
		b= sorted(pre_dict.items(),key=lambda t:t[1])
		h=b[0][0]
		if(completedict[h][0]=='!'):
			new_list=[h]
			while True:
				z=childdict[h]
				new_list.append(z)
				h=z
				if(h==1):
					break
			break
	length =len(new_list)
	new_list.reverse()
	sum=0
	for c in range (0,length):
		a=new_list[c]
		if (c>0):
			v=costdict[a]
			sum = sum + v
			print "Stage %s takes %s seconds" %(c,v)
		print completedict[a]
	print "Total Time taken to pass all the people from one end to other end is %s"%sum
completedict={}
parentdict={}
childdict={}
costdict ={}
childlist = []
dummylist=[]
global incrementor
print"!---The bridge starts here"
total = input('Enter the number of persons to cross the bridge: ')
persons=[]
for i in range(total):
	a=randint(1,50)
	persons.append(a)	
participantsall=persons +['!']
childlist.append(participantsall)
completedict[1]=participantsall
incrementor = 1
parent = []
for p in combinations(persons,2):
	for element in persons:
		if element not in p:
			if "!" in p:
				p = (element,) + p
			else:
				costdict[incrementor+1] = max(p)
				p = ('!',) + p
				p = (element,) + p 
	parent.append(incrementor+1)
	incrementor=incrementor+1
	childdict[incrementor] = 1
	completedict[incrementor]=list(p)
	childlist.append(list(p)) 
parentdict[1] = parent

incrementortt = 0
while True:
	incrementor2=incrementor
	for i in range(incrementor1-1,incrementor2):
		b=childlist[i]
		k= back(b,i+1)
	incrementor1= incrementor2+1
	incrementor2= incrementor
	for i in range(incrementor1,incrementor2+1):
		front(completedict[i],i)
		dummylist=completedict[i]
	if(completedict[incrementor][0]=='!'):
		break	
	incrementor1= incrementor2+1
	incrementortt=incrementortt+1
	
print "Breadth First Search"
start_time1 = time.time()
bredthfirstsearch()
print("--- %s seconds ---" % (time.time() - start_time1))
print "Depth First Search"
start_time2 = time.time()
depthfirstsearch()
print("--- %s seconds ---" % (time.time() - start_time2))

print "Uniform Cost Search"
start_time3 = time.time()
uniformcostsearch()
print("--- %s seconds ---" % (time.time() - start_time3))


	

