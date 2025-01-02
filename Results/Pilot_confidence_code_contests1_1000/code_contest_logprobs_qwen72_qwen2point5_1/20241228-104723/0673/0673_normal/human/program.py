a=map(int,raw_input().split())
b= map(int,raw_input().split())

ans= 0
for i in range(3):
	ans +=abs(a[i]-b[i])

if(ans == 3):
	print("NO")
else:
	print("YES")