#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

for line in stdin:
    a, b, n = (int(s) for s in line.split())
    result = 0
    for i in xrange(1, n+1):
        result += (a * (10 ** i) // b) % 10
    print(result)