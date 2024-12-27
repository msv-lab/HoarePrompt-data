n,q=map(int,raw_input().split())
arr1=list(map(int,raw_input().split()))
arr2=list(map(int,raw_input().split()))
i=0
j=0
ans=n
z=0
while(j<q):
	flag=0
	k=arr2[j]
	sum1=-z
	while(sum1+arr1[i]<=k):
		sum1+=arr1[i]
		ans-=1
		i+=1
		if(ans==0 and sum1<=k):
			flag=1
			ans=n
			i=0
			break
	#print(sum1)
	#print(ans,z,k)
	if(sum1==k):
		z=0
	elif(sum1+arr1[i]>k and flag==0):
		z=k-sum1
	print(ans)
	j+=1










