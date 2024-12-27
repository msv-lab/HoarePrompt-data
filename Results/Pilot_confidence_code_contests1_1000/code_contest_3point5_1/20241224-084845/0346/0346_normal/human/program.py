import sys
n=int(raw_input())
l="abcd"
i=0
flag=0
while i<n:
    x=n/4
    if n<=4:
        x=1
    if x==flag:
        break
    if i==n-1:
        i=0
        flag+=1
    sys.stdout.write(l[i])
    #print l[i],end=""
    i+=1
 	  	 	  					 	 		 		 	 	 	