import math
import collections

n = map(int, raw_input().split())
n = n[0]
c = raw_input()
flag = False
for i in range(n-1):
    if c[i] > c[i+1]:
        flag = True
        pos = i

if flag:
    print("YES")
    print(pos+1,pos+2)
else:
    print("NO")
