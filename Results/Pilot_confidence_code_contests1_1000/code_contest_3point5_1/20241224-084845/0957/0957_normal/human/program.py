T=lambda x: (x*(x+1))//2
t = input()
for _ in xrange(t):
	s = raw_input()
	cur0 = 0
	cur1 = 0
	curQ = 0
	prev = None
	r = 0
	for i in xrange(len(s)):
		c = s[i]
		if i%2 == 0:
			if c == '0':
				if prev == '0':
					cur0 += 1
					curQ = 0
					cur1 = 0
				elif prev == '1':
					r += T(cur1) - T(curQ)
					cur0 += 1
					cur1 = 0
					curQ = 0
					prev = '0'
				else:
					cur0 += 1
				prev = '0'
			elif c == '1':
				if prev == '1':
					cur1 += 1
					curQ = 0
					cur0 = 0
				elif prev == '0':
					r += T(cur0) - T(curQ)
					cur1 += 1
					cur0 = 0
					curQ = 0
				else:
					cur1 += 1
				prev = '1'
			else:
				curQ += 1
				cur0 += 1
				cur1 += 1
		else:
			if c == '1':
				if prev == '0':
					cur0 += 1
					curQ = 0
					cur1 = 0
				elif prev == '1':
					r += T(cur1) - T(curQ)
					cur0 += 1
					cur1 = 0
					curQ = 0
				else:
					cur0 += 1
				prev = '0'
			elif c == '0':
				if prev == '1':
					cur1 += 1
					curQ = 0
					cur0 = 0
				elif prev == '0':
					r += T(cur0) - T(curQ)
					cur1 += 1
					cur0 = 0
					curQ = 0
				else:
					cur1 += 1
				prev = '1'
			else:
				curQ += 1
				cur0 += 1
				cur1 += 1
	if prev is None:
		r += T(curQ)
	elif prev == '1':
		r += T(cur1)
	elif prev == '0':
		r += T(cur0)
	print(r)