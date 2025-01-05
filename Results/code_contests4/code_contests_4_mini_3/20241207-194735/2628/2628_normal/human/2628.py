import sys

n,m = list(map(int,sys.stdin.readline().strip().split(' ')))
a = list(map(int,sys.stdin.readline().strip().split(' ')))
b = list(map(int,sys.stdin.readline().strip().split(' ')))
a = [(a[i*2],a[i*2+1]) for i in range(n)]
b = [(b[i*2],b[i*2+1]) for i in range(m)]

A = [[0,0] for i in range(n)]
B = [[0,0] for i in range(m)]

for i in range(n):
	x1,y1 = a[i]
	for j in range(m):
		x2,y2 = b[j]
		if set(a[i]) != set(b[j]):
			if x1 == x2 or x1 == y2:
				if A[i][1] != 0 and A[i][1] != x1:
					print(-1)
					exit()
				else:
					A[i][0] += 1
					A[i][1] = x1
			elif y1 == x2 or y1 == y2:
				if A[i][1] != 0 and A[i][1] != y1:
					print(-1)
					exit()
				else:
					A[i][0] += 1
					A[i][1] = y1

for i in range(m):
	x1,y1 = b[i]
	for j in range(n):
		x2,y2 = a[j]
		if set(b[i]) != set(a[j]):
			if x1 == x2 or x1 == y2:
				if B[i][1] != 0 and B[i][1] != x1:
					print(-1)
					exit()
				else:
					B[i][0] += 1
					B[i][1] = x1
			elif y1 == x2 or y1 == y2:
				if B[i][1] != 0 and B[i][1] != y1:
					print(-1)
					exit()
				else:
					B[i][0] += 1
					B[i][1] = y1

if sum((A[i][0] for i in range(n))) == 1 or sum((B[i][0] for i in range(m))) == 1:
	for Ai in A:
		if Ai[0] == 1:
			ans = Ai[1]
	for Bi in B:
		if Bi[0] == 1:
			ans = Bi[1]
	print(ans)
else:
	print(0) 