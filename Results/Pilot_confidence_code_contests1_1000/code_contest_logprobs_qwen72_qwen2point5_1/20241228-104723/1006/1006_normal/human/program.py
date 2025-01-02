n=int(raw_input())
a=raw_input().split()
a=[int(a[i]) for i in range(n)]
a.sort()
for i in range(n) :
	print(a[n-i-1]),
print("")

