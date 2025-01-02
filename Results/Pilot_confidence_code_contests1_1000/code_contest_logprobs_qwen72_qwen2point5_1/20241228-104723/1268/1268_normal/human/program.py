#!/usr/bin/env python
#-*- coding: utf-8 -*-

from collections import defaultdict
from math import factorial as f
from fractions import gcd as g

s = raw_input()
t = raw_input()
N, M, ret = len (s), len (t), 0
s = s [::-1]
t = t [::-1]
L = min (N, M)
for i in range (L):
    if s [i] == t [i]:
        ret += 2

ret = N + M - ret
print (ret)
