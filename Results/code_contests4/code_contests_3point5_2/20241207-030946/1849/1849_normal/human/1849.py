from __future__ import print_function
from sys import stdin

rstr = lambda: stdin.readline().strip()
s = rstr()
left, right, sh = s.count('('), s.count(')'), s.count('#')
ans, p = [1] * (sh - 1) + [abs(right - sh - 1)], 0

for j, i in enumerate(s):
    if i == '(':
        left -= 1
    elif i == ')':
        right -= 1
    else:
        right -= ans[p]
        p += 1

    if right > left:
        print(-1)
        exit()

print(*ans, sep='\n')
