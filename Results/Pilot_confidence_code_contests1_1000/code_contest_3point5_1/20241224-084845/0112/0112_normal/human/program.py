import sys

e = ''
def spread(u):
	for v in xrange(1, n+1):
		try:
			x = str(u) + ' ' + str(v)
			y = str(v) + ' ' + str(u)
			if (e.index(x) or e.index(y)) and (u != v):
				if (cl[v] == 0):
					cl[v] = 3-(cl[u])
					spread(v)
				else:
					if cl[v] != 3- cl[u]:
						print ("-1")
						sys.exit(0)

		except ValueError:
			pass
		
			
				

if __name__ == "__main__":
	n, m = map(int, raw_input().split())
	cl = [0] * (n+1)

	hasE = [False] * (n+1)

	for i in xrange(1, m+1):
		u, v = map(int, raw_input().split())
		e += str(u) + ' ' + str(v) + '\n'
		e += str(v) + ' ' + str(u) + '\n'
		hasE[u] = hasE[v] = True

	# print (e)
	for i in xrange(1, n+1):
		if (cl[i] == 0) and (hasE[i]):
			cl[i] = 1
			spread(i)

	stra = ''
	strb = ''
	nA = 0
	nB = 0
	for i in xrange(1, n+1):
		if cl[i] == 1:
			nA += 1
			stra += str(i) + ' '
		elif cl[i] == 2:
			nB += 1
			strb += str(i) + ' '
	print(nA)
	print(stra)
	print(nB)
	print(strb)