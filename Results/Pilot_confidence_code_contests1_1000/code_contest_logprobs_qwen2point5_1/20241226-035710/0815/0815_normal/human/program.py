a = int(raw_input())
arr=list(map(int,raw_input().split(" ")))
s=[]
for i in range(len(arr)):
	if arr[i] not in s:
		s.append(arr[i])
s=sorted(s)
if len(s) >3:
	print(-1)
elif len(s) == 2:
	if sum(s)%2 == 0:
		print((s[1]-s[0])/2)
	else:
		print(s[1]-s[0])
elif len(s) == 3:
	if s[2]-s[1] == s[1]-s[0]:
		print(s[2]-s[1])
	else:
		print(-1)
