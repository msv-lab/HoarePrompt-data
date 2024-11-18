#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

def bomb(surface, x, y):
    surface[y][x] = 0

    start = (x-3) if (x-3) > 0 else 0
    end = (x+4) if (x+4) < 8 else 8
    for i in range(start, end):
        if surface[y][i]:
            bomb(surface, i, y)

    start = (y-3) if (y-3) > 0 else 0
    end = (y+4) if (y+4) < 8 else 8
    for i in range(start, end):
        if surface[i][x]:
            bomb(surface, x, i)

N = int(stdin.readline())
for n in range(1, N+1):
    stdin.readline()

    surface = []
    for _ in range(8):
        surface.append([int(c) for c in stdin.readline().rstrip()])
    x = int(stdin.readline())
    y = int(stdin.readline())

    bomb(surface, x-1, y-1)

    print('Data {}:'.format(n))
    for line in surface:
        print(''.join(str(d) for d in line))