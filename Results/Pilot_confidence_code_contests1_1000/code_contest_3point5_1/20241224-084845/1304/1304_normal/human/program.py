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

n, s, cur, ans = int(input()), rstr(), 0, 'YES'
if '?' in s:
    valid = 0
    for i in range(n):
        if s[i] == '?':
            cur += 1
        else:
            if i and s[i] == s[i - 1] and not cur:
                valid = 0
                break

            if cur > 1 or i == cur or s[i] == s[i - 2]:
                valid += 1

            cur = 0

    print('YES' if valid or cur else 'NO')
else:
    for i in range(1, n):
        if s[i] == s[i - 1]:
            print('NO')
            exit()

    print('YES')
