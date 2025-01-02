from __future__ import division
from sys import stdin, stdout
# from fractions import gcd
# from math import *
# from operator import mul
# from functools import reduce
# from copy import copy
from collections import deque, defaultdict, Counter

rstr = lambda: stdin.readline().strip()
rstrs = lambda: [str(x) for x in stdin.readline().split()]
rint = lambda: int(stdin.readline())
rints = lambda: [int(x) for x in stdin.readline().split()]
rstr_2d = lambda n: [rstr() for _ in range(n)]
rint_2d = lambda n: [rint() for _ in range(n)]
rints_2d = lambda n: [rints() for _ in range(n)]
pr = lambda args, sep: stdout.write(sep.join(map(str, args)) + '\n')
out = []

n, m = rints()
grid, all, ans = rstr_2d(n), [], 'YES'

for i in range(m):
    tem = set()
    for j in range(n):
        if grid[j][i] == '#':
            tem.add(j)

    if tem:
        for j in all:
            inter = tem.intersection(j)
            # print(tem,inter,ans)
            if inter:
                if inter != tem:
                    ans = 'NO'
                break

        if tem not in all:
            all.append(tem)
    # print(all)

print(ans)
