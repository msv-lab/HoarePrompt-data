#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin
from math import cos, sin, atan2, pi

PI2 = pi / 2
L = [None, (1.0, 0.0)]
for _ in range(2, 1001):
    x, y = L[-1]
    rad = atan2(y, x) + PI2
    L.append((x + cos(rad), y + sin(rad)))

for line in stdin:
    n = int(line)
    if n == -1:
        break
    print('{:0.2f}\n{:0.2f}'.format(*L[n]))