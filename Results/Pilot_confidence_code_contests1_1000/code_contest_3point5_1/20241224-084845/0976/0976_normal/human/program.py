n , m , k = [int(x) for x in raw_input().split()]
arr = [int(x) for x in raw_input().split()]
count = 1
while(True):
	if(m+count<n):
		if(arr[m+count]<=k and arr[m+count]!=0):
			print (count+1)*10
			exit()
	if(m-count>0):
		if(arr[m-count]<=k and arr[m-count]!=0):
			print (count+1)*10
			exit()
	count+=1