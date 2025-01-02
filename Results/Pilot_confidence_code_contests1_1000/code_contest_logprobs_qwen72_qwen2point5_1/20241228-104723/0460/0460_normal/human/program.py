from sys import stdin
from collections import *

rints = lambda: [int(x) for x in stdin.readline().split()]
b1, q, l, m = rints()
a, ans, vis = set(rints()), 0, defaultdict(int)

while abs(b1) <= l and vis[b1] < 2:
    if vis[b1] and b1 not in a:
        print('inf')
        exit()

    ans += (b1 not in a and not vis[b1])
    vis[b1] += 1
    b1 *= q

print(ans)
