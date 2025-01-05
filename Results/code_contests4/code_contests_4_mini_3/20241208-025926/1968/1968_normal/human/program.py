from __future__ import division
from sys import stdin, stdout
from collections import *

rstr = lambda: stdin.readline().strip()
rstrs = lambda: [str(x) for x in stdin.readline().split()]
rstr_2d = lambda n: [rstr() for _ in range(n)]
rint = lambda: int(stdin.readline())
rints = lambda: [int(x) for x in stdin.readline().split()]
rint_2d = lambda n: [rint() for _ in range(n)]
rints_2d = lambda n: [rints() for _ in range(n)]
pr = lambda args, sep: stdout.write(sep.join(map(str, args)) + '\n')
ceil1, out = lambda a, b: (a + b - 1) // b, []

for _ in range(int(input())):
    n, a = rint(), sorted(rints())
    be, en, ans = 0, n - 1, n

    while be <= en:
        md = (be + en) >> 1
        su = sum(a[:md + 1])
        for i in range(md + 1, n):
            if su < a[i]:
                su = -1
                break
            su += a[i]

        if su == -1:
            be = md + 1
        else:
            en = md - 1
            ans = md + 1

    out.append(n - ans + 1)
    out.append(' '.join(map(str, [x for x in range(ans, n + 1)])))
pr(out, '\n')
