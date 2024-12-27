#coding:utf-8
one = raw_input().split()
n = int(one[0])
s = int(one[1])
idx = n/2
data = [int(i) for i in raw_input().split()]
newdata = sorted(data)
# print(newdata)
cnt = 0
if newdata[idx] == s:
	print(0)
elif newdata[idx] < s:
	for i in range(idx,n):
		if newdata[i] < s:
			cnt += s - newdata[i]
else:
	for i in range(0,idx+1):
		if newdata[i] > s:
			cnt += newdata[i] - s
print(cnt)
	  	 	  						 	 	 					 	 	 	