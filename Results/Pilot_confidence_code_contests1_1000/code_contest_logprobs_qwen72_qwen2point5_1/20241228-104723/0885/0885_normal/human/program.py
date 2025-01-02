n=raw_input()
a=raw_input()
a=a.split()

n=int(n)
for i in range(n):
	mm=False
	for j in range(i+1,n):
		if a[i]==a[j] and i!=j:
			mm=True
		else:
			if mm==False and i+j==n-1:
				print(a[i])
				