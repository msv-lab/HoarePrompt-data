import math
import collections

n = map(int, raw_input().split())
n = n[0]
c = map(int, raw_input().split())

ans = 0
for i in range(n-2,-1,-1):
    if c[i] != c[i+1]:
        ans = i + 1
        break
print(ans)

