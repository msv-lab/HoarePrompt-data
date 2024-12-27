import sys
import math
 
n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().strip().split(' ')))

possible = True
for i,li in enumerate(l):
	if li > i+1:
		possible = False

if not possible:
	print(-1)
else:
	inf = 10**6
	res = [inf for i in range(n)]

	taken = set(l)

	for i in range(n-1):
		if l[i] != l[i+1]:
			res[i+1] = l[i]

	curr = 0
	while curr in taken:
		curr += 1
	for i in range(n):
		if res[i] == inf:
			res[i] = curr
			curr += 1
			while curr in taken:
				curr += 1

	print(' '.join([str(x) for x in res]))

