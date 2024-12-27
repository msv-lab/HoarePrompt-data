from sys import stdin
from functools import reduce
from fractions import gcd

rint = lambda: int(stdin.readline())
rints = lambda: [int(x) for x in stdin.readline().split()]
rint_2d = lambda n: [rint() for _ in range(n)]
rints_2d = lambda n: [rints() for _ in range(n)]

n, m = rints()
x, p = rints(), rints()
g = reduce(gcd, x)

for i in range(m):
    if g % p[i] == 0:
        print('YES\n%d %d' % (x[0], i + 1))
        exit()
print('NO')
