#!/usr/bin/python2

# Additive cipher

alphabets_s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabets_c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

p=list(raw_input("Enter the plain text:\n(Only Alphabets are allowed)\n").lower())
for each in p:
	if (ord(each)<97) or (ord(each)>122):
		print("Only alphabets allowed !\n")
		exit()
k=int(raw_input("Enter the key value:\n"))
while (k==0 or k>25):
	print "Key should be between 1-25\n"
	k=int(raw_input("Enter the key value:\n"))
p_code=[]
for char in p:
	p_code.append(alphabets_s.index(char))

c_code=[]
for each in p_code:
	c_code.append((each+k)%26)

c=[]
for each in c_code:
	c.append(alphabets_c[each])
print "================================"
print "Cipher text: ", "".join(c)

dcr_msg_code=[]
for each in c_code:
	dcr_msg_code.append((each-k)%26)

dcr_msg=[]
for each in dcr_msg_code:
	dcr_msg.append(alphabets_s[each])

print "Decrypted message: ", "".join(dcr_msg)