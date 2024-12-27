from __future__ import print_function
import math

n,k=map(int,raw_input().split())
a=[int(x) for x in raw_input().split()]


for i in range(1,len(a)):
	if abs(a[i]-a[i-1])>k:
		print("NO")
		exit()

print("YES")
for i in a:
	tmp=1
	for x in range(1,i+1):
		if x>k:
			print(tmp, end=" ")
			tmp+=1
			if tmp>k:
			    tmp=1
			continue
		print(x,end=" ")
	print()	






