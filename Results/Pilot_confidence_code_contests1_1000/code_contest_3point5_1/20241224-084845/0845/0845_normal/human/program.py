#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin
from math import copysign


def gradient(p):
    def fn(t):
        dx = p[0] - t[0]
        dy = p[1] - t[1]
        if dx:
            return dy / dx
        return copysign(float('inf'), -dy)
    return fn


def solve(n):
    L = []
    for i in range(n):
        L.append(tuple(float(s) for s in stdin.readline().split(',')))
    L.sort()

    p = p0 = L.pop(0)
    while True:
        p = max((t for t in L if t[0] >= p[0]), key=gradient(p))
        if p == L[-1]:
            break
        L.remove(p)

    p = p0
    while True:
        p = min((t for t in L if t[0] >= p[0]), key=gradient(p))
        if p == L[-1]:
            break
        L.remove(p)

    return len(L) - 1

while True:
    n = int(stdin.readline())
    if not n:
        break
    print(solve(n))