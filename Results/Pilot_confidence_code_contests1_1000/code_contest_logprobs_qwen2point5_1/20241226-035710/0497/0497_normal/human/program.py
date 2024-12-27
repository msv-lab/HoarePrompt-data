from __future__ import print_function, division
import sys
it = iter(sys.stdin.read().splitlines())
n = int(next(it))
s = next(it)
m = set()
for char in s:
    m.add(char)
k = len(m)
print((k**n) % (10**9 + 7))