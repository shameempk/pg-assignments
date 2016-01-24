#!/usr/bin/python2

# Affine cipher

alphabets_s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabets_c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

k_list=[]
for i in range(26):
	for j in range(26):
		if ((i*j)%26)==1:
			if (i not in k_list):
				k_list.append(i)
			if (j not in k_list):
				k_list.append(j)

p=list(raw_input("Enter the plain text:\n(Only Alphabets are allowed)\n").lower())
for each in p:
	if (ord(each)<97) or (ord(each)>122):
		print("Only alphabets allowed !\n")
		exit()
k1=int(raw_input("Enter the first key - k1:\n(Key should be between 0-25)\n"))

while (k1 not in k_list):
	print "Sorry, provided key is not valid. select key from: ",",".join(map(str,k_list))
	k1=int(raw_input("Enter the key value:\n(Key should be between 0-25)\n"))

for each in k_list:
	if ((each*k1)%26)==1:
		k_inv=each

k2=int(raw_input("Enter the second key - k2:\n"))
while (k2==0 or k2>25):
	print "Key should be between 0-25"
	k2=int(raw_input("Enter the second key - k2:\n"))
p_code=[]
for char in p:
	p_code.append(alphabets_s.index(char))

t_code=[]
for each in p_code:
	t_code.append((each*k1)%26)

c_code=[]
for each in t_code:
	c_code.append((each+k2)%26)

c=[]
for each in c_code:
	c.append(alphabets_c[each])
print "================================"
print "Cipher text: ", "".join(c)

t_dcr_msg_code=[]
for each in c_code:
	t_dcr_msg_code.append((each-k2)%26)

dcr_msg_code=[]
for each in t_dcr_msg_code:
	dcr_msg_code.append((each*k_inv)%26)

dcr_msg=[]
for each in dcr_msg_code:
	dcr_msg.append(alphabets_s[each])

print "Decrypted message: ", "".join(dcr_msg)