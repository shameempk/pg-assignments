#!/usr/bin/python2
nodes=[x for x in raw_input("Enter nodes:\n").split(" ")]
T={}
for each in nodes:
	T[each]=[]
	T[each]=[x for x in raw_input("Enter child nodes of "+each+"\n").split(" ")]

cur_node=raw_input("Enter the node :\n")
ances=[]
def find_ances(node):
	if node==nodes[0]:
		return 0
	else:
		for each in T:
			if node in T[each]:
				ances.append(each)
				find_ances(each)

find_ances(cur_node)

for x in range(len(ances)):
	print "Ancestor"+str(x+1)+ " of "+cur_node+" : "+ances[x]
