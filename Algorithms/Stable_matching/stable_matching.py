#!/usr/bin/python2
'''The preference list must be sorted in reverse order. ie, most prefered option should be at the last. This is beacause of the stack usage.'''
import json

data=open('stable_matching_input.json').read()
input_data=json.loads(data)

#Dictionaries of stored pref. lists
pref_list_m = input_data['pref_list_m']
pref_list_w = input_data['pref_list_w']

#Dictionaries to store current pairs
cur_m={}
cur_w={}

#List of Men and Women
men=input_data['men']
women=input_data['women']

#Initializing all as free 
for each in men:
	cur_m[each]=False
for each in women:
	cur_w[each]=False
def match():
	for each in men:
		if cur_m[each]==False:

			
			#POP the next prefered woman
			w=pref_list_m[each].pop()
			# print each,w
			if cur_w[w]==False:
				cur_m[each]=w
				cur_w[w]=each
			elif (pref_list_w[w].index(each)>pref_list_w[w].index(cur_w[w])):
				cur_m[cur_w[w]]=False
				cur_m[each]=w
				cur_w[w]=each
			else:
				pass
	for x in men:
		if cur_m[x]==False:
			match()
match()



print "The Matched pairs :\n"
for men in cur_m:
	print men+" : "+cur_m[men]
