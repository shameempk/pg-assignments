#!/usr/bin/python3
#Autokey cipher

p=list(input("Enter the plain text:\n(Only Alphabets are allowed)\n").lower().replace(" ",""))
for each in p:
	if (ord(each)<97) or (ord(each)>122):
		print("Only alphabets allowed !\n")
		exit()
k=int(input("Enter the key value:\n"))
while (k==0 or k>25):
	print("Key should be between 1-25\n")
	k=int(input("Enter the key value:\n"))
	
p_code=[(ord(a)-97) for a in p]

c_code=[(p_code[0]+k)%26]

for i in range(1,len(p_code)):
	c_code.append((p_code[i]+p_code[i-1])%26)

c=[chr(a+97) for a in c_code]

print("Cipher Text: ","".join(c).upper())

dcr_msg_code=[(((ord(c[0])-97)-k)%26)]
for i in range(1,len(c)):
	dcr_msg_code.append((((ord(c[i])-97)-dcr_msg_code[i-1])%26))

dcr_msg=[chr(a+97) for a in dcr_msg_code]

print("Decrypted message: ","".join(dcr_msg))
