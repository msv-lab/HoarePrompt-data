mod = 1000000007
res = 1
ca = 1
s = raw_input()
for i in s:
	if i == 'a':
		ca+=1
	elif i == 'b':
		res = (res*ca)%mod
		ca = 1
res = (res*ca)%mod
print (res-1)%mod
		 		 			 			 	 	      				 			