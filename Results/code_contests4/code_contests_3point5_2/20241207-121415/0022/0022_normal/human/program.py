n = input()
p = []
h = []

for i in range(n):
	e = map(int,raw_input().split())
	p.append(e[0])
	h.append(e[1])
	
pivout = p[0]

if (n == 1):
	cont = 1
else:
	cont = 2

for i in range(1,len(p)-1):
	if ((p[i] - h[i]) > pivout):
		cont+=1
		pivout = p[i]
	elif ((p[i] + h[i]) < p[i+1]):
		cont+=1
		pivout = p[i]+h[i]
	else:
		pivout = p[i]

print(cont)
		
	
	
	
