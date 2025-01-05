#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

for line in stdin:
    q = int(line)
    if q == -1:
        break

    x = q / 2.0
    diff = q * 0.00001
    while True:
        x = x - (x**3 - q) / (3 * x * x)
        if abs(x**3 - q) < diff:
            break
    print('{:.6f}'.format(x))