from sys import *

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
last = arr[n - 1]
for i in range(n - 1, -1, -1):
	if arr[i] > last:
		d = arr[i] - last
		if d > 1:
			print("No")
			exit(0)
	last = min(last, arr[i])
print("Yes")