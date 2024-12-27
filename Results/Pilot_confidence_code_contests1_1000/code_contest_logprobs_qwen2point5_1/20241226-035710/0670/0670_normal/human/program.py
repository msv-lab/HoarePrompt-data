[n]=[int(i) for i in raw_input().split()]
ans=1
i=1
step=2
while(i<n):
    ans+=step
    ans=ans%1000000007
    step+=i
    i+=1
print(ans%1000000007)
					   	  	 		 		 		 		  	