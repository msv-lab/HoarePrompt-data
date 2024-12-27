#!/usr/bin/env python

import sys
import math
import itertools as it
from collections import deque

sys.setrecursionlimit(10000000)

while True:
    n, k, m = map(int, raw_input().split())
    if n == 0:
        break

    pos = 0
    for num in range(1, n):
        pos += k
        pos %= num
    ans = (m + pos) % n + 1
    
