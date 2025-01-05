from __future__ import print_function, division
import sys
from __builtin__ import xrange as range
from future_builtins import ascii, filter, hex, map, oct, zip
input = lambda: sys.stdin.readline().rstrip("\r\n")
from functools import reduce
a = int(input())
i = 0
while i < a :
    b = int(input())
    s = b
    g = ""
    g = g + str(b)
    while ((s-1) > 0) and (b % 2 == 0) :
        s = s - 1
        g = g + " "
        g = g + str(s)
    while ((s-1) > 0) and (b % 2 == 1) :
        s = s - 1
        if s == ((b//2)+1) :
            g = g + " "
            g = g + str(s - 1)
            g = g + " "
            g = g + str(s)
            s = s - 2
        if s == 0 :
            break
        g = g + " "
        g = g + str(s)
    print(g)
    i = i + 1



