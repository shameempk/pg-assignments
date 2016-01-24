#!/usr/bin/python3
import socket
import sys
import numpy
import math
import fractions

print("HILL CIPHER\n")

def k_preprocess(k):
	while len(k)<math.pow(math.ceil(math.sqrt(len(k))),2):
		k+="x"
	n=int(math.sqrt(len(k)))
	k_matrix=[k[i:i+n] for i in range(0,len(k),n)]
	k_matrix_code=[[ord(a)-97 for a in l] for l in k_matrix]
	return k_matrix_code

def hill_cipher_ecr(p,k_matrix_code):
	n=len(k_matrix_code)
	if (len(p)%n):
		p=p+['x' for i in range(n-(len(p)%n))]
	p_matrix=[p[i:i+n] for i in range(0,len(p),n)]
	p_matrix_code=[[ord(a)-97 for a in l] for l in p_matrix]
	c_matrix_code=[(n%26 for n in numpy.matmul(k_matrix_code,a)) for a in p_matrix_code]
	c_matrix=[[chr(b+97) for b in l] for l in c_matrix_code]
	return c_matrix
	

def hill_cipher_dcr(c,k_matrix_code):
	c=c.lower()
	n=len(k_matrix_code)
	det_k=int(numpy.linalg.det(k_matrix_code))
	k_matrix_code_og_inv=numpy.linalg.inv(k_matrix_code)
	k_matrix_code_adj=[[(x*det_k) for x in l] for l in k_matrix_code_og_inv]
	for i in range(1,26):
		if (i*det_k)%26==1:
			det_inv=i
			break
	k_matrix_code_inv=[[int(round(det_inv*n%26)) for n in l] for l in k_matrix_code_adj]
	c_matrix=[c[i:i+n] for i in range(0,len(c),n)]
	c_matrix_code=[[ord(a)-97 for a in l] for l in c_matrix]
	d_matrix_code=[(n%26 for n in numpy.matmul(k_matrix_code_inv,a)) for a in c_matrix_code]
	d_matrix=[[chr(b+97) for b in l] for l in d_matrix_code]
	return d_matrix

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
	p=list(input("Enter the plain text:\n(Only Alphabets are allowed)\n").replace(" ","").lower())
	k=list(input("Enter the key text:\n(Only Alphabets are allowed)\n").replace(" ","").lower())
	k_matrix_code=k_preprocess(k)
	det_k=int(numpy.linalg.det(k_matrix_code))
	if fractions.gcd(det_k,26)>1:
		print("Invalid key ! ")
		exit()
	if det_k:
		c_mat=hill_cipher_ecr(p,k_matrix_code)
		print("Encrypted message: ")
		c=""
		for l in c_mat:
			c+="".join(l).upper()
		print(c)
	else:
		print("Key matrix is not invertible !")
		exit()

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
	k_matrix_code=k_preprocess(k)
	det_k=int(numpy.linalg.det(k_matrix_code))
	if fractions.gcd(det_k,26)>1:
		print("Invalid key ! ")
		exit()
	if det_k:
		d_mat=hill_cipher_dcr(c,k_matrix_code)
		d=""
		for l in d_mat:
			d+="".join(l)
		print("Decrypted message: ",d)
	else:
		print("Key matrix is not invertible !")
		exit()
	s.close()