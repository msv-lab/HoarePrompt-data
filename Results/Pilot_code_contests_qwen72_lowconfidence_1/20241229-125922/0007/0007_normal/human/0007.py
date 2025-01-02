import sys
import math
from collections import defaultdict

n,k = list(map(int, sys.stdin.readline().strip().split(' ')))

t = []
a = []
b = []
for _ in range(n):
	ti,ai,bi = list(map(int, sys.stdin.readline().strip().split(' ')))
	t.append(ti)
	a.append(ai)
	b.append(bi)

alice_only = []
alice = 0
bob = 0
bob_only = []
taken = [0 for i in range(n)]
ts = sorted(enumerate(t), key=lambda x: x[1])
for i,ti in ts:
	if a[i] and b[i]:
		if alice == k and bob == k:
			if alice_only and bob_only:
				if ti < alice_only[-1] + bob_only[-1]:
					taken[alice_only.pop()] = 0
					taken[bob_only.pop()] = 0
					taken[i] = 1
			continue
		if alice == k:
			if alice_only:
				j = alice_only.pop()
				taken[j] = 0
		else:
			alice += 1
		if bob == k:
			if bob_only:
				j = bob_only.pop()
				taken[j] = 0
		else:
			bob += 1
		taken[i] = 1
		continue
	if a[i] and alice < k:
		alice += 1
		alice_only.append(i)
		taken[i] = 1
	if b[i] and bob < k:
		bob += 1
		bob_only.append(i)
		taken[i] = 1

if alice != k or bob != k:
	print(-1)
else:
	ans = 0
	for i,ti in ts:
		if taken[i]:
			ans += ti
	print(ans)





