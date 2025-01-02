from __future__ import print_function
from collections import Counter

n = input()
dom, vyezd = Counter(), Counter()
for i in range(n):
    a, b = map(int, raw_input().split())
    dom[a] += 1
    vyezd[b] += 1
    
otv = 0
for i in dom:
    otv += vyezd[i]

print(otv)
