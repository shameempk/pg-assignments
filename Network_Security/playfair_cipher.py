#!/usr/bin/python3
import socket
import sys
import math
def p_preprocess(p):
	for i in range(len(p)):
		if i>0:
			if p[i]==cur and p[i]!='x':
				#Inserting x in place of repeating consequetive letters
				p=p[:i]+'x'+p[i:]
		cur=p[i]
	if len(p)%2:
		#Two make digram even length is required
		p+='x'
	return p
def get_letter_pos(plfr_mat):
	letter_pos={}
	# Following finds out the position of each chars in playfair matrix
	for rows in plfr_mat:
		for char in rows:
			row=plfr_mat.index(rows)
			col=rows.index(char)
			letter_pos[char]=[row,col]

	letter_pos['j']=letter_pos['i'] # i and j are interchangable 
	return letter_pos
def make_plfr_mat(k):
	plfr_mat_string=""
	for each in k:
		if (each not in plfr_mat_string) and each!="J":
			# key string is filled with letters in k , without repetation
			# 'J' is avoided and I is only considered
			plfr_mat_string+=each

	plfr_mat_string=plfr_mat_string.lower()
	for i in range(97,123):
		# key string is filled with remaining chars in alphabet
		if (len(plfr_mat_string)<=25 and i!=106):
			if chr(i) not in plfr_mat_string:
				plfr_mat_string+=(chr(i))
	# playfair string is made , and now it is getting chopped down to matrix of 5x5
	plfr_mat=[plfr_mat_string[i:i+5] for i in range(0,len(plfr_mat_string),5)]
	return plfr_mat
def plfr_ecr(p,k):
	plfr_mat=make_plfr_mat(k)
	# Converting plaintext into digrams
	p_digrm=[]
	for i in range(0,len(p),2):
		p_digrm.append(p[i:i+2])
	# Getting letter positions for each letters in playfair matrix
	letter_pos=get_letter_pos(plfr_mat)
	c=[]
	for digrm in p_digrm:
		for a,b in digrm.split():
			row_a=letter_pos[a][0]
			col_a=letter_pos[a][1]
			row_b=letter_pos[b][0]
			col_b=letter_pos[b][1]
			if row_a==row_b:
				# same row
				c.append(plfr_mat[row_a][(col_a+1)%5]+plfr_mat[row_b][(col_b+1)%5])
			elif col_a==col_b:
				#same column
				c.append(plfr_mat[(row_a+1)%5][col_a]+plfr_mat[(row_b+1)%5][col_b])
			else:
				# The rectangle case
				c.append(plfr_mat[row_a][col_b]+plfr_mat[row_b][col_a])
	c=" ".join(c).upper()
	return c

def plfr_dcr(c,k):
	c=c.lower().replace(" ","")
	plfr_mat=make_plfr_mat(k)
	c_digrm=[]
	for i in range(0,len(c),2):
		c_digrm.append(c[i:i+2])
	letter_pos=get_letter_pos(plfr_mat)
	d=[]	
	for digrm in c_digrm:
		for a,b in digrm.split():
			row_a=letter_pos[a][0]
			col_a=letter_pos[a][1]
			row_b=letter_pos[b][0]
			col_b=letter_pos[b][1]
			if row_a==row_b:
				# same row
				d.append(plfr_mat[row_a][(col_a+4)%5]+plfr_mat[row_b][(col_b+4)%5])
			elif col_a==col_b:
				#same column
				d.append(plfr_mat[(row_a+4)%5][col_a]+plfr_mat[(row_b+4)%5][col_b])
			else:
				# The rectangle case
				d.append(plfr_mat[row_a][col_b]+plfr_mat[row_b][col_a])
	d="".join(d)
	return d

print("PLAYFAIR CIPHER\n")



while (len(sys.argv)<=1 or (sys.argv[1] not in ['-s','-r'])):
	print("Usage: "+sys.argv[0]+" <mode> <ip address> <port>\nmodes:\n-s: send\n-r: receive")
	exit()
mode=sys.argv[1]
s=socket.socket()
if(mode=="-s"):
	ip=sys.argv[2]
	port=int(sys.argv[3])
	try:
		s.connect((ip,port))
	except:
		print("Receiver is not ready !")
		exit()

	p=input("Enter the plain text:\n(Only Alphabets are allowed)\n").replace(" ","").lower()
	p=p_preprocess(p)
	k=list(input("Enter the key text:\n(Only Alphabets are allowed)\n").replace(" ","").lower())
	c=plfr_ecr(p,k)
	if len(c):
		print("Encrypted message: ",c)
		s.send(c.encode('ascii'))
	s.close()
if(mode=="-r"):
	host = socket.gethostname() 
	port = 12345                
	s.bind((host, port))   
	s.listen()
	print("Waiting for incoming message\n")
	conn, addr = s.accept()
	c = conn.recv(1024)
	c=c.decode('ascii')
	if len(c): print("\nEncrypted message received.\n")
	k=list(input("Enter the key to decrypt:\n").replace(" ","").lower())
	d=plfr_dcr(c,k)
	print("Decrypted message: ",d)
