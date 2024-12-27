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

n, a, b = rints()
s = rints()
ext, ans, su = (a * s[0]) // b, 0, sum(s)
for i in sorted(s[1:])[::-1]:
    if su <= ext:
        break
    su -= i
    ans += 1
print(ans)
