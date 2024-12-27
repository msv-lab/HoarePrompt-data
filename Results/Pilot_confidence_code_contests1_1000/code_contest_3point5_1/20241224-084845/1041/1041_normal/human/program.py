def solve(string):
    
	a = 0
	b = 0
	c = 0
	v = 1
	MOD = 10**9 + 7
	for i in string:
		if i == 'a':
			a += v
		elif i == 'b':
			b += a
		elif i == 'c':
			c += b
		else:
			a,b,c,v = (3*a+v)%MOD, (3*b+a)%MOD, (3*c+b)%MOD, (3*v)%MOD
	return c % MOD
n = int(raw_input())
tmp = raw_input()
print(solve(tmp))