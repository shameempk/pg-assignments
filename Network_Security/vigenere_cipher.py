#!/usr/bin/python3
#Vigenere cipher

p=list(input("Enter the plain text:\n(Only Alphabets are allowed)\n").lower())
for each in p:
	if (ord(each)<97) or (ord(each)>122):
		print("Only alphabets allowed !\n")
		exit()
k=list(input("Enter the key string:\n").lower())
for each in k:
	if (ord(each)<97) or (ord(each)>122):
		print("Only alphabets allowed !\n")
		exit()	
p_code=[(ord(a)-97) for a in p]
k_code=[(ord(a)-97) for a in k]
c_code=[]
for i in range(len(p)):
	c_code.append((p_code[i]+k_code[i%len(k)])%26)

c=[chr(a+97) for a in c_code]
print("Cipher Text: ","".join(c).upper())

dcr_msg_code=[]
for i in range(len(c)):
	dcr_msg_code.append(((ord(c[i])-97)-k_code[i%len(k)])%26)
dcr_msg=[chr(a+97) for a in dcr_msg_code]
print("Decrypted message: ","".join(dcr_msg))