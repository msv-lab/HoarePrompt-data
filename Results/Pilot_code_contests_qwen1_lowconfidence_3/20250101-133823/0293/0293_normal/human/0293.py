def multy(a,b):
	c = 0
	for i in range(len(a)):
		c += a[i]*b[i]
	return c
N,M = map(int, raw_input().split())
ks = []
for i in range(M):
	ks2 = map(int, raw_input().split())
	ks.append(ks2)
pm = map(int, raw_input().split())
plist = []
for i in ks:
	t = [0]*N
	ini = 1
	for j in i:
		if(ini == 1):
			ini = 0
			continue
		else:
			t[j-1] = 1
	plist.append(t)
slist = []
for i in range(2**N):
	t = []
	for j in range(N):
		t.append(i%2)
		i = i/2
	slist.append(t)
r = 0
for p in plist:
	s2 = []
	for s in slist:
		if(multy(p,s)%2 == pm[r]):
			s2.append(s)
	r = r+1
	slist = s2
print(len(slist))