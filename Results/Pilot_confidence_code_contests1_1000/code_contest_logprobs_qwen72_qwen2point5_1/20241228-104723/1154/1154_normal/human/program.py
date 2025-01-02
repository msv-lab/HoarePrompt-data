import sys

n,k=map(int,raw_input().split())
a=list(map(int,raw_input().split()))
max_sum=1
summ=1
for i in xrange(1,len(a)):
	if a[i]!=a[i-1]:
		summ+=1
		if max_sum<summ:
			max_sum=summ
	else:
		summ=1
print(max_sum)