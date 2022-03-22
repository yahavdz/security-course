from __future__ import print_function  
import os
import random
numfiles = 10
#good = random.randrange(numfiles)
#print ("good: " + str(good))
for i in range(numfiles):
	f = open("/home/ubuntu/environment/machon_lev_cyber_labs/exercises/lab4_RSA/lab4_challenge/message"+str(i)+".txt","r+")
	#f.write (str(random.randrange(10000)))
	fileContent = f.read()
	f.close()
	# $ $ openssl dgst -sha256 -verify my-pub.pem -signature in.txt.sha256 in.txt  
 
	print("verify for %s" % str(i))
	os.system("openssl dgst -sha512 -verify ./lab4_public.pem -signature ./message" + str(i) + ".txt.sign" + " message"+str(i)+".txt")
	#f = open("message"+str(i)+".txt","r+")
	#c = f.read(1)
	#print (str(i) + ":" + str(c))
	#f.seek(0,0)
	#if i != good:
	#	f.write (str((int(c) + 1) % 10))
	#f.close()


