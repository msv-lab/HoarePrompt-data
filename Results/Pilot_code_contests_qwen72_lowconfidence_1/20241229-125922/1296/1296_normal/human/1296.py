import heapq

n, k = [int(x) for x in raw_input().split()]
hLst = [int(x) for x in raw_input().split()]
a = i = j = 0
r = []
m = M = hLst[0]
mI = MI = 0
q1 = []
q2 = []
while j < n:
	w = hLst[j]
	if w <= m:
		m = w
		mI = j
	if w >= M:
		M = w
		MI = j
	heapq.heappush(q1, (w, j))
	heapq.heappush(q2, (-w, j))
	prevJ = j
	if M-m > k:
		break
	j += 1
while j < n:
	if j-i > a:
		a = j-i
		r = [(i+1, j)]
	elif j-i == a:
		r.append((i+1, j))
	if j-i == 1:
		m = M = hLst[j]
		mI = MI = j
		i += 1
	elif mI < MI:
		i = mI+1
		w, t = heapq.heappop(q1)
		while t < i:
			w, t = heapq.heappop(q1)
		heapq.heappush(q1, (w, t))
		m = w
		mI = t
		w, t = heapq.heappop(q2)
		while t < i:
			w, t = heapq.heappop(q2)
		heapq.heappush(q2, (w, t))
	else:
		i = MI+1
		w, t = heapq.heappop(q2)
		while t < i:
			w, t = heapq.heappop(q2)
		heapq.heappush(q2, (w, t))
		M = -w
		MI = t
		w, t = heapq.heappop(q1)
		while t < i:
			w, t = heapq.heappop(q1)
		heapq.heappush(q1, (w, t))
	while j < n:
		w = hLst[j]
		if w <= m:
			m = w
			mI = j
		if w >= M:
			M = w
			MI = j
		if prevJ != j:
			heapq.heappush(q1, (w, j))
			heapq.heappush(q2, (-w, j))
			prevJ = j
		if M-m > k:
			break
		j += 1
if j-i > a:
	a = j-i
	r = [(i+1, j)]
elif j-i == a:
	r.append((i+1, j))
	
print(str(a)+' '+str(len(r)))
for x in r:
	print(str(x[0])+' '+str(x[1]))