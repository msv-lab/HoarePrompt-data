from __future__ import print_function
from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
n, m = rints()
a, t, mem, ans = rints(), rints(), [], [0] * m

for i in range(n + m - 1, -1, -1):
    if t[i]:
        mem.append(a[i])

cur, l = mem.pop(), 0

for i in range(n + m):
    if not t[i]:
        while mem:
            if abs(cur - a[i]) > abs(mem[-1] - a[i]):
                cur = mem.pop()
                l += 1
            else:
                break
        ans[l] += 1

print(' '.join(map(str, ans)))
