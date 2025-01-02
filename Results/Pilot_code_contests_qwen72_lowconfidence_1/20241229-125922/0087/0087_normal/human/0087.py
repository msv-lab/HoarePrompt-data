#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin


def print_time_lefts(seconds):
    h, remain = divmod(7200 - seconds, 3600)
    m, s = divmod(remain, 60)
    print('{:02d}:{:02d}:{:02d}'.format(h, m, s))

for line in stdin:
    h, m, s = (int(s) for s in line.split())
    if h == -1 and m == -1 and s == -1:
        break
    seconds = h * 3600 + m * 60 + s
    print_time_lefts(seconds)
    print_time_lefts(seconds // 3)