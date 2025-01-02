#!/usr/bin/env python
import math

nl = raw_input().split(" ")
n = nl[0]
l = nl[1]

a = raw_input().split(" ")

d = []
j = 0
while 1==1:
    co = 0
    for i in range(len(a)):
        co += int(int(a[i])/(int(l) + j))
        
    d.append(co)
    j += 1
    if co == 0:
        break

d.sort()
o = d[len(d) - 1] * int(l)
print(str(o))