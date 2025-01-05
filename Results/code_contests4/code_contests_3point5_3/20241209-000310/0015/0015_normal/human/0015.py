c=raw_input()
p=c.split()
num=[]
for i in p:
    num.append(int(i))

y=float(num[0]*num[2])/float(100)-num[1]

if y%1==0:
    print(int(y))
else:
    print(int(y)+1)

 	 		  	  	 		  					 		  		  	