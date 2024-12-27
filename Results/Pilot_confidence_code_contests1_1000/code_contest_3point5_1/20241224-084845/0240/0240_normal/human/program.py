from math import *
from Queue import *
from sys import *


def update(l):
    new = []
    new.append(l[0])
    for i in range(1,len(l)-1):
        new.append((l[i-1]+l[i]+l[i+1])/2)
    new.append(l[-1])
    return new
        
        

n = int(raw_input())
l = map(int, raw_input().split())
br = []
for i in range(n-1):
    if l[i] == l[i+1]:
        br.append(i+1)
c = []
for i in range(len(br)-1):
    if br[i+1] == br[i] + 1:
        pass
    else:
        c.append((br[i+1] - br[i] - 2)/2)
if len(c) == 0:
    m = (n-1)/2
else:
    m = max(c)
for i in range(m):
    l = update(l)
print(m)
print(' '.join(map(str, l)))
