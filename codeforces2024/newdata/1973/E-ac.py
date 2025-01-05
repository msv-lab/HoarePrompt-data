ans = []
 
for t in range(int(input())):
	n = int(input())
	p = [int(x) for x in input().split()]
 
	total = 2*n + n*(2*n-1)
 
	#l = r
	trick = -1
	unsort = []
	for i in range(n):
		if p[i] == i+1:
			continue
		unsort.append(i+1)
		if trick == -1:
			trick = i+1+p[i]
		elif not trick == i+1+p[i]:
			trick = -2
	if trick > 0: total -= (2*n-1)
	if trick == -2: total -= 2*n
 
	if len(unsort) > 0:
		a = n - unsort[0]
		total -= a*(a-1)//2
		b = unsort[-1]
		total -= b*(b-1)//2
 
	ans.append(total)
		
 
for a in ans:
	print(a)