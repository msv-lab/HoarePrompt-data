import sys

a = [True] * 1000000

for i in range(2,1000000):
	if(a[i-1]):
		for j in range(i**2-1, 1000000, i):
			a[j] = False

for s in sys.stdin:
	print(a[1:int(s)].count(True))