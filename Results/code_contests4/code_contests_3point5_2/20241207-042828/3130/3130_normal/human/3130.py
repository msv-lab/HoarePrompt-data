from sys import stdin
from collections import *

n, a = int(input()), [int(x) for x in stdin.readline().split()]
out, que = [-1] * n, deque()
for i in range(n):
    if not a[i]:
        que.append((i, 0))

while que:
    ix, lev = que.popleft()
    if out[ix] != -1:
        out[ix] = lev
        if 0 <= ix + 1 <= n - 1:
            que.append((ix + 1, lev + 1))
        if 0 <= ix - 1 <= n - 1:
            que.append((ix - 1, lev + 1))

print(' '.join(map(str, out)))
