#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

s = 0
for line in stdin:
    digit = bytearray()
    for c in line:
        if c.isdigit():
            digit.append(c)
        elif digit:
            s += int(digit)
            digit = bytearray()

print(s)