import sys

t = 0
T = 0
a = None
b = None
d = set()
for line in sys.stdin:
	line = line.strip()
	if t == 0: 
		T = int(line)
		a = [0]*(T+1)
		b = [0]*(T+1)
	elif line:
		i,j = [int(item) for item in line.split()]
		d.add((i,j))
		a[i] += 1
		a[j] += 1
	else:
		break
	t += 1
for i,j in d:
	b[j] += a[i]
	b[i] += a[j]
print (sum(b)-sum(a)) /2



