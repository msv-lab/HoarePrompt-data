import sys
from math import ceil

def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(i*i, limit, i):
                a[n] = False
    return a

def solution(x2):
	x1s = set([])
	for p in primes:
		if x2%p:
			continue
		for x1 in range(x2-p+1,x2):
			x1s.add(x1)
	x1s = list(x1s)
	min_x0 = float('inf')
	for x1 in x1s[1000:]:
		for p in primes:
			if x1%p:
				continue
			if x1 == p:
				if x1 < 3:
					continue
				min_x0 = min(min_x0, x1)
			else:
				if x1-p+1 < 3:
					continue
				min_x0 = min(min_x0, x1-p+1)
	return min_x0

primes = primes_sieve(1000001)
x2 = int(sys.stdin.readline().strip())
primes = [i for i,p in enumerate(primes) if p == True and i <= x2+1]
print(solution(x2))

